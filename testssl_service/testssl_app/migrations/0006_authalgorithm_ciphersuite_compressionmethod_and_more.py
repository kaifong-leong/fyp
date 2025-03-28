# Generated by Django 5.1 on 2025-03-07 06:46

import django.db.models.deletion
import markdownx.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testssl_app', '0005_urlitem_cert_urlitem_cert_sig_alg_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthAlgorithm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('long_name', models.CharField(max_length=300)),
                ('quantum_strength', models.IntegerField(default=0, null=True)),
                ('hybrid', models.BooleanField(default=False, null=True)),
            ],
            options={
                'verbose_name': 'authentication algorithm',
                'verbose_name_plural': 'authentication algorithms',
                'ordering': ['short_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CipherSuite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('long_name', models.CharField(max_length=300)),
                ('hex_byte_1', models.CharField(max_length=4)),
                ('hex_byte_2', models.CharField(max_length=4)),
                ('security', models.IntegerField(blank=True, choices=[(0, 'recommended'), (1, 'secure'), (2, 'weak'), (3, 'insecure')], default=3, verbose_name='security level')),
                ('auth_algorithm', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='testssl_app.authalgorithm')),
            ],
            options={
                'verbose_name': 'cipher suite',
                'verbose_name_plural': 'cipher suites',
                'ordering': ['short_name'],
            },
        ),
        migrations.CreateModel(
            name='CompressionMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('long_name', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'compression method',
                'verbose_name_plural': 'compression methods',
                'ordering': ['short_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DHKeyLength',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('long_name', models.CharField(max_length=300)),
                ('classical_strength', models.IntegerField(default=0, null=True)),
                ('quantum_strength', models.IntegerField(default=0, null=True)),
            ],
            options={
                'verbose_name': 'DH key length',
                'verbose_name_plural': 'DH key lengths',
                'ordering': ['short_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ECNamedCurve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('long_name', models.CharField(max_length=300)),
                ('quantum_strength', models.IntegerField(default=0, null=True)),
                ('classical_strength', models.IntegerField(default=0, null=True)),
                ('hybrid', models.BooleanField(default=False, null=True)),
            ],
            options={
                'verbose_name': 'EC named curve',
                'verbose_name_plural': 'EC named curves',
                'ordering': ['short_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EncAlgorithm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('long_name', models.CharField(max_length=300)),
                ('classical_strength', models.IntegerField(default=0, null=True)),
                ('quantum_strength', models.IntegerField(default=0, null=True)),
                ('aead_algorithm', models.BooleanField(default=False, null=True)),
            ],
            options={
                'verbose_name': 'encryption algorithm',
                'verbose_name_plural': 'encryption algorithms',
                'ordering': ['short_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HashAlgorithm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('long_name', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'hash algorithm',
                'verbose_name_plural': 'hash algorithms',
                'ordering': ['short_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KexAlgorithm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('long_name', models.CharField(max_length=300)),
                ('pfs_support', models.BooleanField(default=False, null=True)),
                ('quantum_strength', models.IntegerField(default=0, null=True)),
                ('hybrid', models.BooleanField(default=False, null=True)),
            ],
            options={
                'verbose_name': 'key exchange algorithm',
                'verbose_name_plural': 'key exchange algorithms',
                'ordering': ['short_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RSAKeyLength',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('long_name', models.CharField(max_length=300)),
                ('classical_strength', models.IntegerField(default=0, null=True)),
                ('quantum_strength', models.IntegerField(default=0, null=True)),
            ],
            options={
                'verbose_name': 'RSA key length',
                'verbose_name_plural': 'RSA key lengths',
                'ordering': ['short_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TLSProtocolVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('long_name', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'TLS protocol variant',
                'verbose_name_plural': 'TLS protocol variants',
                'ordering': ['short_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TLSProtocolVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.PositiveIntegerField()),
                ('minor', models.PositiveIntegerField()),
                ('short', models.PositiveIntegerField(unique=True)),
                ('short_name', models.CharField(db_index=True, default='', max_length=255)),
            ],
            options={
                'verbose_name': 'TLS version',
                'verbose_name_plural': 'TLS versions',
                'ordering': ['major', 'minor'],
            },
        ),
        migrations.CreateModel(
            name='Vulnerability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', markdownx.models.MarkdownxField(blank=True, max_length=1000)),
                ('severity', models.IntegerField(choices=[(2, 'High'), (1, 'Medium'), (0, 'Low')], default=0)),
            ],
            options={
                'verbose_name': 'vulnerability',
                'verbose_name_plural': 'vulnerabilities',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='X509Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fingerprint', models.CharField(max_length=200, unique=True)),
                ('issuer', models.CharField(default='', max_length=200)),
                ('subject', models.CharField(default='', max_length=200)),
                ('serial_number', models.CharField(default='', max_length=200)),
                ('not_valid_before', models.DateTimeField(default=None, null=True)),
                ('not_valid_after', models.DateTimeField(default=None, null=True)),
                ('key_length', models.IntegerField(null=True)),
                ('key_algorithm', models.CharField(blank=True, default='', max_length=200)),
                ('key_type', models.CharField(blank=True, default='', max_length=200)),
                ('exponent', models.CharField(default='', max_length=200)),
                ('cert_dump', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'certificate',
                'verbose_name_plural': 'certificates',
            },
        ),
        migrations.DeleteModel(
            name='Policy',
        ),
        migrations.DeleteModel(
            name='PolicyRule',
        ),
        migrations.DeleteModel(
            name='Rule',
        ),
        migrations.DeleteModel(
            name='Subrule',
        ),
        migrations.AddField(
            model_name='ciphersuite',
            name='enc_algorithm',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='testssl_app.encalgorithm'),
        ),
        migrations.AddField(
            model_name='ciphersuite',
            name='hash_algorithm',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='testssl_app.hashalgorithm'),
        ),
        migrations.AddField(
            model_name='ecnamedcurve',
            name='kex_algorithm',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='testssl_app.kexalgorithm'),
        ),
        migrations.AddField(
            model_name='ciphersuite',
            name='kex_algorithm',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='testssl_app.kexalgorithm'),
        ),
        migrations.AddField(
            model_name='ciphersuite',
            name='protocol_variant',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='testssl_app.tlsprotocolvariant'),
        ),
        migrations.AddField(
            model_name='ciphersuite',
            name='tls_version',
            field=models.ManyToManyField(blank=True, to='testssl_app.tlsprotocolversion'),
        ),
        migrations.AddField(
            model_name='tlsprotocolversion',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='testssl_app.vulnerability'),
        ),
        migrations.AddField(
            model_name='tlsprotocolvariant',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='testssl_app.vulnerability'),
        ),
        migrations.AddField(
            model_name='rsakeylength',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='testssl_app.vulnerability'),
        ),
        migrations.AddField(
            model_name='kexalgorithm',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='testssl_app.vulnerability'),
        ),
        migrations.AddField(
            model_name='hashalgorithm',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='testssl_app.vulnerability'),
        ),
        migrations.AddField(
            model_name='encalgorithm',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='testssl_app.vulnerability'),
        ),
        migrations.AddField(
            model_name='ecnamedcurve',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='testssl_app.vulnerability'),
        ),
        migrations.AddField(
            model_name='dhkeylength',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='testssl_app.vulnerability'),
        ),
        migrations.AddField(
            model_name='compressionmethod',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='testssl_app.vulnerability'),
        ),
        migrations.AddField(
            model_name='ciphersuite',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='testssl_app.vulnerability'),
        ),
        migrations.AddField(
            model_name='authalgorithm',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='testssl_app.vulnerability'),
        ),
        migrations.AddField(
            model_name='x509certificate',
            name='auth_algorithm',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certificates_as_auth_algorithm', to='testssl_app.authalgorithm'),
        ),
        migrations.AddField(
            model_name='x509certificate',
            name='curve',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='testssl_app.ecnamedcurve'),
        ),
        migrations.AddField(
            model_name='x509certificate',
            name='hash_algorithm',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certificates_as_hash_algorithm', to='testssl_app.hashalgorithm'),
        ),
        migrations.AlterUniqueTogether(
            name='ciphersuite',
            unique_together={('hex_byte_1', 'hex_byte_2')},
        ),
    ]
