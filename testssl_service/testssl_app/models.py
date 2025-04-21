from django.db import models
from django.utils import timezone

class URLItem(models.Model):
    url = models.CharField(max_length=200, verbose_name="URL")
    date = models.DateTimeField(default=timezone.now)
    value_sslv2 = models.CharField(max_length=100, default="not offered")
    value_sslv3 = models.CharField(max_length=100, default="not offered")
    value_tls1 = models.CharField(max_length=100, default="not offered")
    value_tls11 = models.CharField(max_length=100, default="not offered")
    value_tls12 = models.CharField(max_length=100, default="not offered")
    value_tls13 = models.CharField(max_length=100, default="not offered")
    tls10_ciphers = models.CharField(max_length=10000, default="not offered")
    tls11_ciphers = models.CharField(max_length=10000, default="not offered")
    tls12_ciphers = models.CharField(max_length=10000, default="not offered")
    tls13_ciphers = models.CharField(max_length=10000, default="not offered")
    kems = models.CharField(max_length=10000, default="not offered")
    ecdhe_curves = models.CharField(max_length=10000, default="none")
    tls12_sig_alg = models.CharField(max_length=10000, default="none")
    tls13_sig_alg = models.CharField(max_length=10000, default="none")
    cert_sig_alg = models.CharField(max_length=10000, default="none")
    cert = models.CharField(max_length=10000, default="none")

    def __str__(self):
        return self.url
    
class TestsslScan(models.Model):
    url = models.CharField(max_length=200, verbose_name="URL")
    date = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.url

"""
class TLSProtocolVersion(models.model): 
    major = models.IntegerField()
    minor = models.IntegerField()
    
class KEX():
    pass

class TestsslScan(models.Model):
    versions = models.ManyToManyField(
        TLSProtocolVersion,
        # to add values for TLSProtocolVersion, eg. offered/not offered
    )

    kexs = models.ManyToManyField(
        KEX,
        # to add values for KEX
    )

# Database will look like the following
TestsslScan_someNewId | version_someId | not_offered
TestsslScan_someNewId | version_someOtherId | offered  
"""

# class Policy(models.Model):
#     name = models.CharField(max_length=200)


#     def __str__(self):
#         return self.name
    
# class PolicyRule(models.Model):
#     name = models.CharField(max_length=200)


#     def __str__(self):
#         return self.name
    
# class Rule(models.Model):
#     name = models.CharField(max_length=200)


#     def __str__(self):
#         return self.name
    
# class Subrule(models.Model):
#     name = models.CharField(max_length=200)


#     def __str__(self):
#         return self.name
    
"""Models Defined:
- PrintableModel: Abstract model class that provides
    a to_dict method to convert model instance to dictionary
- Rfc: Model to store RFCs
- CryptoAsset: Abstract model class that stores common
    fields for all crypto assets

# core crypto assets
- KexAlgorithm
- AuthAlgorithm
- EncAlgorithm
- HashAlgorithm
- ECNamedCurve
- X509Certificate

# crypto assets related to TLS
- CompressionMethod
- TLSProtocolVersion
- CipherSuite

- Vulnerability: Model to store publicly available vulnerabilities

"""

# from django.utils import timezone
# from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.utils.translation import gettext_lazy as _
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class PrintableModel(models.Model):
    class Meta:
        abstract = True

    def to_dict(self):
        opts = self._meta
        data = {}
        for f in opts.concrete_fields + opts.many_to_many:
            if isinstance(f, ManyToManyField):
                if self.pk is None:
                    data[f.name] = []
                else:
                    data[f.name] = [
                        x.__str__() for x in list(f.value_from_object(self))
                    ]
            else:
                data[f.name] = f.value_from_object(self)
        return data


class CryptoAssetManager(models.Manager):
    def get_by_natural_key(self, short_name):
        return self.get(short_name=short_name)


class CryptoAsset(PrintableModel):
    short_name = models.CharField(
        unique=True,
        max_length=200,
        db_index=True,
    )
    long_name = models.CharField(
        max_length=300,
    )
    vulnerabilities = models.ManyToManyField(
        "Vulnerability",
        blank=True,
    )

    objects = CryptoAssetManager()

    class Meta:
        abstract = True
        ordering = ["short_name"]

    def __str__(self):
        return self.short_name

    def __lt__(self, other):
        return self.short_name < other.short_name

    def natural_key(self):
        return (self.short_name,)


class KexAlgorithm(CryptoAsset):
    pfs_support = models.BooleanField(
        default=False,
        null=True,
    )
    quantum_strength = models.IntegerField(
        default=0,
        null=True,
    )
    hybrid = models.BooleanField(
        default=False,
        null=True,
    )

    class Meta(CryptoAsset.Meta):
        verbose_name = _("key exchange algorithm")
        verbose_name_plural = _("key exchange algorithms")


class AuthAlgorithm(CryptoAsset):
    quantum_strength = models.IntegerField(
        default=0,
        null=True,
    )
    hybrid = models.BooleanField(
        default=False,
        null=True,
    )

    class Meta(CryptoAsset.Meta):
        verbose_name = _("authentication algorithm")
        verbose_name_plural = _("authentication algorithms")


class EncAlgorithm(CryptoAsset):
    classical_strength = models.IntegerField(
        default=0,
        null=True,
    )
    quantum_strength = models.IntegerField(
        default=0,
        null=True,
    )
    aead_algorithm = models.BooleanField(
        default=False,
        null=True,
    )

    class Meta(CryptoAsset.Meta):
        verbose_name = _("encryption algorithm")
        verbose_name_plural = _("encryption algorithms")


class HashAlgorithm(CryptoAsset):
    class Meta(CryptoAsset.Meta):
        verbose_name = _("hash algorithm")
        verbose_name_plural = _("hash algorithms")


class ECNamedCurve(CryptoAsset):
    quantum_strength = models.IntegerField(
        default=0,
        null=True,
    )
    classical_strength = models.IntegerField( # fixed typo from clasical to classical
        default=0,
        null=True,
    )
    hybrid = models.BooleanField(
        default=False,
        null=True,
    )
    kex_algorithm = models.ForeignKey(
        "KexAlgorithm",
        on_delete=models.CASCADE,
        blank=True,
        default=None,
        null=True,
    )

    class Meta(CryptoAsset.Meta):
        verbose_name = _("EC named curve")
        verbose_name_plural = _("EC named curves")


class RSAKeyLength(CryptoAsset):
    classical_strength = models.IntegerField(
        default=0,
        null=True,
    )
    quantum_strength = models.IntegerField(
        default=0,
        null=True,
    )

    class Meta(CryptoAsset.Meta):
        verbose_name = _("RSA key length")
        verbose_name_plural = _("RSA key lengths")


class DHKeyLength(CryptoAsset):
    classical_strength = models.IntegerField(
        default=0,
        null=True,
    )
    quantum_strength = models.IntegerField(
        default=0,
        null=True,
    )

    class Meta(CryptoAsset.Meta):
        verbose_name = _("DH key length")
        verbose_name_plural = _("DH key lengths")


class X509Certificate(PrintableModel):
    fingerprint = models.CharField(
        max_length=200,
        unique=True,
    )
    issuer = models.CharField(
        max_length=200,
        default="",
    )
    subject = models.CharField(
        max_length=200,
        default="",
    )
    serial_number = models.CharField(
        max_length=200,
        default="",
    )
    not_valid_before = models.DateTimeField(
        default=None,
        null=True,
    )
    not_valid_after = models.DateTimeField(
        default=None,
        null=True,
    )
    key_length = models.IntegerField(
        null=True,
    )
    key_algorithm = models.CharField(
        max_length=200,
        blank=True,
        default="",
    )
    key_type = models.CharField(
        max_length=200,
        blank=True,
        default="",
    )

    auth_algorithm = models.ForeignKey(
        "AuthAlgorithm",
        related_name="certificates_as_auth_algorithm",
        on_delete=models.CASCADE,
        null=True,
        default=None,
    )
    hash_algorithm = models.ForeignKey(
        "HashAlgorithm",
        related_name="certificates_as_hash_algorithm",
        on_delete=models.CASCADE,
        null=True,
        default=None,
    )
    curve = models.ForeignKey(
        "ECNamedCurve",
        on_delete=models.CASCADE,
        blank=True,
        default=None,
        null=True,
    )
    exponent = models.CharField(
        max_length=200,
        default="",
    )
    cert_dump = models.TextField(
        default="",
    )

    class Meta:
        verbose_name = _("certificate")
        verbose_name_plural = _("certificates")

    def __str__(self):
        return self.subject


# TLS related models
class TLSProtocolVariant(CryptoAsset):  # export or standard
    class Meta(CryptoAsset.Meta):
        verbose_name = _("TLS protocol variant")
        verbose_name_plural = _("TLS protocol variants") # fixed spelling form varaints to variants


class TLSProtocolVersionManager(models.Manager):
    def get_by_natural_key(self, short):
        return self.get(short=short)


class TLSProtocolVersion(models.Model):
    major = models.PositiveIntegerField()
    minor = models.PositiveIntegerField()
    short = models.PositiveIntegerField(
        unique=True,
    )
    short_name = models.CharField(max_length=255, db_index=True, default="")

    vulnerabilities = models.ManyToManyField(
        "Vulnerability",
        blank=True,
    )

    objects = TLSProtocolVersionManager()

    class Meta:
        verbose_name = _("TLS version")
        verbose_name_plural = _("TLS versions")
        ordering = ["major", "minor"]

    def __str__(self):
        ssl_versions_major = [2, 3]
        if self.major in ssl_versions_major:
            return f"SSLv{self.major}.{self.minor}"

        return f"TLSv{self.major}.{self.minor}"

    def save(self, *args, **kwargs):
        if not self.short_name:
            self.short_name = str(self)
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.short,)


class CompressionMethod(CryptoAsset):
    class Meta(CryptoAsset.Meta):
        verbose_name = _("compression method")
        verbose_name_plural = _("compression methods")

class CipherSuite(CryptoAsset):
    # hex bytes stored as string 0x00-0xFF
    hex_byte_1 = models.CharField(
        max_length=4,
    )
    hex_byte_2 = models.CharField(
        max_length=4,
    )
    protocol_variant = models.ForeignKey(
        "TLSProtocolVariant",
        on_delete=models.CASCADE,
        blank=True,
        default="",
    )
    tls_version = models.ManyToManyField(
        TLSProtocolVersion,
        blank=True,
    )
    kex_algorithm = models.ForeignKey(
        "KexAlgorithm",
        on_delete=models.CASCADE,
        blank=True,
        default="",
    )
    auth_algorithm = models.ForeignKey(
        "AuthAlgorithm",
        on_delete=models.CASCADE,
        blank=True,
        default="",
    )
    enc_algorithm = models.ForeignKey(
        "EncAlgorithm",
        on_delete=models.CASCADE,
        blank=True,
        default="",
    )
    hash_algorithm = models.ForeignKey(
        "HashAlgorithm",
        on_delete=models.CASCADE,
        blank=True,
        default="",
    )
    # security level
    REC = 0
    SEC = 1
    WEK = 2
    INS = 3
    SECURITY_CHOICES = (
        (REC, "recommended"),
        (SEC, "secure"),
        (WEK, "weak"),
        (INS, "insecure"),
    )
    security = models.IntegerField(
        verbose_name=_("security level"),
        choices=SECURITY_CHOICES,
        default=3,
        blank=True,
        editable=True,
    )

    class Meta:
        ordering = ["short_name"]
        verbose_name = _("cipher suite")
        verbose_name_plural = _("cipher suites")
        # hex bytes identifiy cipher suite uniquely
        unique_together = (("hex_byte_1", "hex_byte_2"),)

    def __str__(self):
        return self.short_name

    @property
    def recommended(self):
        return self.security == 0

    @property
    def secure(self):
        return self.security == 1

    @property
    def weak(self):
        return self.security == 2  # noqa:PLR2004

    @property
    def insecure(self):
        return self.security == 3  # noqa:PLR2004

    @property
    def tls10_cipher(self):
        v0 = TLSProtocolVersion.objects.get(major=1, minor=0)
        v1 = TLSProtocolVersion.objects.get(major=1, minor=1)
        return v0 in self.tls_version.all() or v1 in self.tls_version.all()

    @property
    def tls12_cipher(self):
        v = TLSProtocolVersion.objects.get(major=1, minor=2)
        return v in self.tls_version.all()

    @property
    def tls13_cipher(self):
        v = TLSProtocolVersion.objects.get(major=1, minor=3)
        return v in self.tls_version.all()


class VulnerabilityManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Vulnerability(PrintableModel):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    description = MarkdownxField(
        max_length=1000,
        blank=True,
    )

    SEVERITY_CHOICES = (
        (2, "High"),
        (1, "Medium"),
        (0, "Low"),
    )
    severity = models.IntegerField(
        choices=SEVERITY_CHOICES,
        default=0,
    )

    objects = VulnerabilityManager()

    class Meta:
        ordering = ["name"]
        verbose_name = _("vulnerability")
        verbose_name_plural = _("vulnerabilities")

    def __str__(self):
        return self.name

    @property
    def formatted_desc(self):
        return markdownify(self.description)

    def natural_key(self):
        return (self.name,)
