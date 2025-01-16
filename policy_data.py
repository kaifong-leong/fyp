# Define possible values for each rule
POSSIBLE_TLS_VERSIONS = ("SSL 2.0", "SSL 3.0", "TLS 1.0", "TLS 1.1", "TLS 1.2", "TLS 1.3")
POSSIBLE_CERTIFICATE_TYPES = ("ecdsa", "dsa", "rsa", "ecdh", "dh")
POSSIBLE_TLS_SUPPORTED_GROUPS = ("sect163k1", "sect163r1", "sect163r2", "sect193r1", "sect193r2", "sect233k1", "sect233r1", "sect239k1", "sect283k1", "sect283r1", "sect409k1", "sect409r1", "sect571k1", "sect571r1", "secp160k1", "secp160r1", "secp160r2", "secp192k1", "secp192r1", "secp224k1", "secp224r1", "secp256k1", "secp256r1", "secp384r1", "secp521r1", "brainpoolP256r1", "brainpoolP384r1", "brainpoolP512r1", "x25519", "x448", "brainpoolP256r1tls13", "brainpoolP384r1tls13", "brainpoolP512r1tls13", "GC256A", "GC256B", "GC256C", "GC256D", "GC512A", "GC512B", "GC512C", "curveSM2", "ffdhe2048", "ffdhe3072", "ffdhe4096", "ffdhe6144", "ffdhe8192", "MLKEM512", "MLKEM768", "MLKEM1024", "SecP256r1MLKEM768", "X25519MLKEM768", "X25519Kyber768Draft00 (OBSOLETE)", "SecP256r1Kyber768Draft00 (OBSOLETE)", "arbitrary_explicit_prime_curves", "arbitrary_explicit_char2_curves")
POSSIBLE_TLS_CIPHERSUITES = ("TLS_NULL_WITH_NULL_NULL", "TLS_RSA_WITH_NULL_MD5", "TLS_RSA_WITH_NULL_SHA", "TLS_RSA_EXPORT_WITH_RC4_40_MD5", "TLS_RSA_WITH_RC4_128_MD5", "TLS_RSA_WITH_RC4_128_SHA", "TLS_RSA_EXPORT_WITH_RC2_CBC_40_MD5", "TLS_RSA_WITH_IDEA_CBC_SHA", "TLS_RSA_EXPORT_WITH_DES40_CBC_SHA", "TLS_RSA_WITH_DES_CBC_SHA", "TLS_RSA_WITH_3DES_EDE_CBC_SHA", "TLS_DH_DSS_EXPORT_WITH_DES40_CBC_SHA", "TLS_DH_DSS_WITH_DES_CBC_SHA", "TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA", "TLS_DH_RSA_EXPORT_WITH_DES40_CBC_SHA", "TLS_DH_RSA_WITH_DES_CBC_SHA", "TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA", "TLS_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA", "TLS_DHE_DSS_WITH_DES_CBC_SHA", "TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA", "TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA", "TLS_DHE_RSA_WITH_DES_CBC_SHA", "TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA", "TLS_DH_anon_EXPORT_WITH_RC4_40_MD5", "TLS_DH_anon_WITH_RC4_128_MD5", "TLS_DH_anon_EXPORT_WITH_DES40_CBC_SHA", "TLS_DH_anon_WITH_DES_CBC_SHA", "TLS_DH_anon_WITH_3DES_EDE_CBC_SHA", "TLS_KRB5_WITH_DES_CBC_SHA", "TLS_KRB5_WITH_3DES_EDE_CBC_SHA", "TLS_KRB5_WITH_RC4_128_SHA", "TLS_KRB5_WITH_IDEA_CBC_SHA", "TLS_KRB5_WITH_DES_CBC_MD5", "TLS_KRB5_WITH_3DES_EDE_CBC_MD5", "TLS_KRB5_WITH_RC4_128_MD5", "TLS_KRB5_WITH_IDEA_CBC_MD5", "TLS_KRB5_EXPORT_WITH_DES_CBC_40_SHA", "TLS_KRB5_EXPORT_WITH_RC2_CBC_40_SHA", "TLS_KRB5_EXPORT_WITH_RC4_40_SHA", "TLS_KRB5_EXPORT_WITH_DES_CBC_40_MD5", "TLS_KRB5_EXPORT_WITH_RC2_CBC_40_MD5", "TLS_KRB5_EXPORT_WITH_RC4_40_MD5", "TLS_PSK_WITH_NULL_SHA", "TLS_DHE_PSK_WITH_NULL_SHA", "TLS_RSA_PSK_WITH_NULL_SHA", "TLS_RSA_WITH_AES_128_CBC_SHA", "TLS_DH_DSS_WITH_AES_128_CBC_SHA", "TLS_DH_RSA_WITH_AES_128_CBC_SHA", "TLS_DHE_DSS_WITH_AES_128_CBC_SHA", "TLS_DHE_RSA_WITH_AES_128_CBC_SHA", "TLS_DH_anon_WITH_AES_128_CBC_SHA", "TLS_RSA_WITH_AES_256_CBC_SHA", "TLS_DH_DSS_WITH_AES_256_CBC_SHA", "TLS_DH_RSA_WITH_AES_256_CBC_SHA", "TLS_DHE_DSS_WITH_AES_256_CBC_SHA", "TLS_DHE_RSA_WITH_AES_256_CBC_SHA", "TLS_DH_anon_WITH_AES_256_CBC_SHA", "TLS_RSA_WITH_NULL_SHA256", "TLS_RSA_WITH_AES_128_CBC_SHA256", "TLS_RSA_WITH_AES_256_CBC_SHA256", "TLS_DH_DSS_WITH_AES_128_CBC_SHA256", "TLS_DH_RSA_WITH_AES_128_CBC_SHA256", "TLS_DHE_DSS_WITH_AES_128_CBC_SHA256", "TLS_RSA_WITH_CAMELLIA_128_CBC_SHA", "TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA", "TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA", "TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA", "TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA", "TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA", "TLS_DHE_RSA_WITH_AES_128_CBC_SHA256", "TLS_DH_DSS_WITH_AES_256_CBC_SHA256", "TLS_DH_RSA_WITH_AES_256_CBC_SHA256", "TLS_DHE_DSS_WITH_AES_256_CBC_SHA256", "TLS_DHE_RSA_WITH_AES_256_CBC_SHA256", "TLS_DH_anon_WITH_AES_128_CBC_SHA256", "TLS_DH_anon_WITH_AES_256_CBC_SHA256", "TLS_RSA_WITH_CAMELLIA_256_CBC_SHA", "TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA", "TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA", "TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA", "TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA", "TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA", "TLS_PSK_WITH_RC4_128_SHA", "TLS_PSK_WITH_3DES_EDE_CBC_SHA", "TLS_PSK_WITH_AES_128_CBC_SHA", "TLS_PSK_WITH_AES_256_CBC_SHA", "TLS_DHE_PSK_WITH_RC4_128_SHA", "TLS_DHE_PSK_WITH_3DES_EDE_CBC_SHA", "TLS_DHE_PSK_WITH_AES_128_CBC_SHA", "TLS_DHE_PSK_WITH_AES_256_CBC_SHA", "TLS_RSA_PSK_WITH_RC4_128_SHA", "TLS_RSA_PSK_WITH_3DES_EDE_CBC_SHA", "TLS_RSA_PSK_WITH_AES_128_CBC_SHA", "TLS_RSA_PSK_WITH_AES_256_CBC_SHA", "TLS_RSA_WITH_SEED_CBC_SHA", "TLS_DH_DSS_WITH_SEED_CBC_SHA", "TLS_DH_RSA_WITH_SEED_CBC_SHA", "TLS_DHE_DSS_WITH_SEED_CBC_SHA", "TLS_DHE_RSA_WITH_SEED_CBC_SHA", "TLS_DH_anon_WITH_SEED_CBC_SHA", "TLS_RSA_WITH_AES_128_GCM_SHA256", "TLS_RSA_WITH_AES_256_GCM_SHA384", "TLS_DHE_RSA_WITH_AES_128_GCM_SHA256", "TLS_DHE_RSA_WITH_AES_256_GCM_SHA384", "TLS_DH_RSA_WITH_AES_128_GCM_SHA256", "TLS_DH_RSA_WITH_AES_256_GCM_SHA384", "TLS_DHE_DSS_WITH_AES_128_GCM_SHA256", "TLS_DHE_DSS_WITH_AES_256_GCM_SHA384", "TLS_DH_DSS_WITH_AES_128_GCM_SHA256", "TLS_DH_DSS_WITH_AES_256_GCM_SHA384", "TLS_DH_anon_WITH_AES_128_GCM_SHA256", "TLS_DH_anon_WITH_AES_256_GCM_SHA384", "TLS_PSK_WITH_AES_128_GCM_SHA256", "TLS_PSK_WITH_AES_256_GCM_SHA384", "TLS_DHE_PSK_WITH_AES_128_GCM_SHA256", "TLS_DHE_PSK_WITH_AES_256_GCM_SHA384", "TLS_RSA_PSK_WITH_AES_128_GCM_SHA256", "TLS_RSA_PSK_WITH_AES_256_GCM_SHA384", "TLS_PSK_WITH_AES_128_CBC_SHA256", "TLS_PSK_WITH_AES_256_CBC_SHA384", "TLS_PSK_WITH_NULL_SHA256", "TLS_PSK_WITH_NULL_SHA384", "TLS_DHE_PSK_WITH_AES_128_CBC_SHA256", "TLS_DHE_PSK_WITH_AES_256_CBC_SHA384", "TLS_DHE_PSK_WITH_NULL_SHA256", "TLS_DHE_PSK_WITH_NULL_SHA384", "TLS_RSA_PSK_WITH_AES_128_CBC_SHA256", "TLS_RSA_PSK_WITH_AES_256_CBC_SHA384", "TLS_RSA_PSK_WITH_NULL_SHA256", "TLS_RSA_PSK_WITH_NULL_SHA384", "TLS_RSA_WITH_CAMELLIA_128_CBC_SHA256", "TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA256", "TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA256", "TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA256", "TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA256", "TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA256", "TLS_RSA_WITH_CAMELLIA_256_CBC_SHA256", "TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA256", "TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA256", "TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA256", "TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA256", "TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA256", "TLS_SM4_GCM_SM3", "TLS_SM4_CCM_SM3", "TLS_EMPTY_RENEGOTIATION_INFO_SCSV", "TLS_AES_128_GCM_SHA256", "TLS_AES_256_GCM_SHA384", "TLS_CHACHA20_POLY1305_SHA256", "TLS_AES_128_CCM_SHA256", "TLS_AES_128_CCM_8_SHA256", "TLS_AEGIS_256_SHA512", "TLS_AEGIS_128L_SHA256", "TLS_FALLBACK_SCSV", "TLS_ECDH_ECDSA_WITH_NULL_SHA", "TLS_ECDH_ECDSA_WITH_RC4_128_SHA", "TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA", "TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA", "TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA", "TLS_ECDHE_ECDSA_WITH_NULL_SHA", "TLS_ECDHE_ECDSA_WITH_RC4_128_SHA", "TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA", "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA", "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA", "TLS_ECDH_RSA_WITH_NULL_SHA", "TLS_ECDH_RSA_WITH_RC4_128_SHA", "TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA", "TLS_ECDH_RSA_WITH_AES_128_CBC_SHA", "TLS_ECDH_RSA_WITH_AES_256_CBC_SHA", "TLS_ECDHE_RSA_WITH_NULL_SHA", "TLS_ECDHE_RSA_WITH_RC4_128_SHA", "TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA", "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA", "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA", "TLS_ECDH_anon_WITH_NULL_SHA", "TLS_ECDH_anon_WITH_RC4_128_SHA", "TLS_ECDH_anon_WITH_3DES_EDE_CBC_SHA", "TLS_ECDH_anon_WITH_AES_128_CBC_SHA", "TLS_ECDH_anon_WITH_AES_256_CBC_SHA", "TLS_SRP_SHA_WITH_3DES_EDE_CBC_SHA", "TLS_SRP_SHA_RSA_WITH_3DES_EDE_CBC_SHA", "TLS_SRP_SHA_DSS_WITH_3DES_EDE_CBC_SHA", "TLS_SRP_SHA_WITH_AES_128_CBC_SHA", "TLS_SRP_SHA_RSA_WITH_AES_128_CBC_SHA", "TLS_SRP_SHA_DSS_WITH_AES_128_CBC_SHA", "TLS_SRP_SHA_WITH_AES_256_CBC_SHA", "TLS_SRP_SHA_RSA_WITH_AES_256_CBC_SHA", "TLS_SRP_SHA_DSS_WITH_AES_256_CBC_SHA", "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256", "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384", "TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256", "TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384", "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256", "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384", "TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256", "TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384", "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256", "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256", "TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256", "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384", "TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256", "TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_PSK_WITH_RC4_128_SHA", "TLS_ECDHE_PSK_WITH_3DES_EDE_CBC_SHA", "TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA", "TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA", "TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA256", "TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384", "TLS_ECDHE_PSK_WITH_NULL_SHA", "TLS_ECDHE_PSK_WITH_NULL_SHA256", "TLS_ECDHE_PSK_WITH_NULL_SHA384", "TLS_RSA_WITH_ARIA_128_CBC_SHA256", "TLS_RSA_WITH_ARIA_256_CBC_SHA384", "TLS_DH_DSS_WITH_ARIA_128_CBC_SHA256", "TLS_DH_DSS_WITH_ARIA_256_CBC_SHA384", "TLS_DH_RSA_WITH_ARIA_128_CBC_SHA256", "TLS_DH_RSA_WITH_ARIA_256_CBC_SHA384", "TLS_DHE_DSS_WITH_ARIA_128_CBC_SHA256", "TLS_DHE_DSS_WITH_ARIA_256_CBC_SHA384", "TLS_DHE_RSA_WITH_ARIA_128_CBC_SHA256", "TLS_DHE_RSA_WITH_ARIA_256_CBC_SHA384", "TLS_DH_anon_WITH_ARIA_128_CBC_SHA256", "TLS_DH_anon_WITH_ARIA_256_CBC_SHA384", "TLS_ECDHE_ECDSA_WITH_ARIA_128_CBC_SHA256", "TLS_ECDHE_ECDSA_WITH_ARIA_256_CBC_SHA384", "TLS_ECDH_ECDSA_WITH_ARIA_128_CBC_SHA256", "TLS_ECDH_ECDSA_WITH_ARIA_256_CBC_SHA384", "TLS_ECDHE_RSA_WITH_ARIA_128_CBC_SHA256", "TLS_ECDHE_RSA_WITH_ARIA_256_CBC_SHA384", "TLS_ECDH_RSA_WITH_ARIA_128_CBC_SHA256", "TLS_ECDH_RSA_WITH_ARIA_256_CBC_SHA384", "TLS_RSA_WITH_ARIA_128_GCM_SHA256", "TLS_RSA_WITH_ARIA_256_GCM_SHA384", "TLS_DHE_RSA_WITH_ARIA_128_GCM_SHA256", "TLS_DHE_RSA_WITH_ARIA_256_GCM_SHA384", "TLS_DH_RSA_WITH_ARIA_128_GCM_SHA256", "TLS_DH_RSA_WITH_ARIA_256_GCM_SHA384", "TLS_DHE_DSS_WITH_ARIA_128_GCM_SHA256", "TLS_DHE_DSS_WITH_ARIA_256_GCM_SHA384", "TLS_DH_DSS_WITH_ARIA_128_GCM_SHA256", "TLS_DH_DSS_WITH_ARIA_256_GCM_SHA384", "TLS_DH_anon_WITH_ARIA_128_GCM_SHA256", "TLS_DH_anon_WITH_ARIA_256_GCM_SHA384", "TLS_ECDHE_ECDSA_WITH_ARIA_128_GCM_SHA256", "TLS_ECDHE_ECDSA_WITH_ARIA_256_GCM_SHA384", "TLS_ECDH_ECDSA_WITH_ARIA_128_GCM_SHA256", "TLS_ECDH_ECDSA_WITH_ARIA_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_ARIA_128_GCM_SHA256", "TLS_ECDHE_RSA_WITH_ARIA_256_GCM_SHA384", "TLS_ECDH_RSA_WITH_ARIA_128_GCM_SHA256", "TLS_ECDH_RSA_WITH_ARIA_256_GCM_SHA384", "TLS_PSK_WITH_ARIA_128_CBC_SHA256", "TLS_PSK_WITH_ARIA_256_CBC_SHA384", "TLS_DHE_PSK_WITH_ARIA_128_CBC_SHA256", "TLS_DHE_PSK_WITH_ARIA_256_CBC_SHA384", "TLS_RSA_PSK_WITH_ARIA_128_CBC_SHA256", "TLS_RSA_PSK_WITH_ARIA_256_CBC_SHA384", "TLS_PSK_WITH_ARIA_128_GCM_SHA256", "TLS_PSK_WITH_ARIA_256_GCM_SHA384", "TLS_DHE_PSK_WITH_ARIA_128_GCM_SHA256", "TLS_DHE_PSK_WITH_ARIA_256_GCM_SHA384", "TLS_RSA_PSK_WITH_ARIA_128_GCM_SHA256", "TLS_RSA_PSK_WITH_ARIA_256_GCM_SHA384", "TLS_ECDHE_PSK_WITH_ARIA_128_CBC_SHA256", "TLS_ECDHE_PSK_WITH_ARIA_256_CBC_SHA384", "TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_CBC_SHA256", "TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_CBC_SHA384", "TLS_ECDH_ECDSA_WITH_CAMELLIA_128_CBC_SHA256", "TLS_ECDH_ECDSA_WITH_CAMELLIA_256_CBC_SHA384", "TLS_ECDHE_RSA_WITH_CAMELLIA_128_CBC_SHA256", "TLS_ECDHE_RSA_WITH_CAMELLIA_256_CBC_SHA384", "TLS_ECDH_RSA_WITH_CAMELLIA_128_CBC_SHA256", "TLS_ECDH_RSA_WITH_CAMELLIA_256_CBC_SHA384", "TLS_RSA_WITH_CAMELLIA_128_GCM_SHA256", "TLS_RSA_WITH_CAMELLIA_256_GCM_SHA384", "TLS_DHE_RSA_WITH_CAMELLIA_128_GCM_SHA256", "TLS_DHE_RSA_WITH_CAMELLIA_256_GCM_SHA384", "TLS_DH_RSA_WITH_CAMELLIA_128_GCM_SHA256", "TLS_DH_RSA_WITH_CAMELLIA_256_GCM_SHA384", "TLS_DHE_DSS_WITH_CAMELLIA_128_GCM_SHA256", "TLS_DHE_DSS_WITH_CAMELLIA_256_GCM_SHA384", "TLS_DH_DSS_WITH_CAMELLIA_128_GCM_SHA256", "TLS_DH_DSS_WITH_CAMELLIA_256_GCM_SHA384", "TLS_DH_anon_WITH_CAMELLIA_128_GCM_SHA256", "TLS_DH_anon_WITH_CAMELLIA_256_GCM_SHA384", "TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_GCM_SHA256", "TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_GCM_SHA384", "TLS_ECDH_ECDSA_WITH_CAMELLIA_128_GCM_SHA256", "TLS_ECDH_ECDSA_WITH_CAMELLIA_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_CAMELLIA_128_GCM_SHA256", "TLS_ECDHE_RSA_WITH_CAMELLIA_256_GCM_SHA384", "TLS_ECDH_RSA_WITH_CAMELLIA_128_GCM_SHA256", "TLS_ECDH_RSA_WITH_CAMELLIA_256_GCM_SHA384", "TLS_PSK_WITH_CAMELLIA_128_GCM_SHA256", "TLS_PSK_WITH_CAMELLIA_256_GCM_SHA384", "TLS_DHE_PSK_WITH_CAMELLIA_128_GCM_SHA256", "TLS_DHE_PSK_WITH_CAMELLIA_256_GCM_SHA384", "TLS_RSA_PSK_WITH_CAMELLIA_128_GCM_SHA256", "TLS_RSA_PSK_WITH_CAMELLIA_256_GCM_SHA384", "TLS_PSK_WITH_CAMELLIA_128_CBC_SHA256", "TLS_PSK_WITH_CAMELLIA_256_CBC_SHA384", "TLS_DHE_PSK_WITH_CAMELLIA_128_CBC_SHA256", "TLS_DHE_PSK_WITH_CAMELLIA_256_CBC_SHA384", "TLS_RSA_PSK_WITH_CAMELLIA_128_CBC_SHA256", "TLS_RSA_PSK_WITH_CAMELLIA_256_CBC_SHA384", "TLS_ECDHE_PSK_WITH_CAMELLIA_128_CBC_SHA256", "TLS_ECDHE_PSK_WITH_CAMELLIA_256_CBC_SHA384", "TLS_RSA_WITH_AES_128_CCM", "TLS_RSA_WITH_AES_256_CCM", "TLS_DHE_RSA_WITH_AES_128_CCM", "TLS_DHE_RSA_WITH_AES_256_CCM", "TLS_RSA_WITH_AES_128_CCM_8", "TLS_RSA_WITH_AES_256_CCM_8", "TLS_DHE_RSA_WITH_AES_128_CCM_8", "TLS_DHE_RSA_WITH_AES_256_CCM_8", "TLS_PSK_WITH_AES_128_CCM", "TLS_PSK_WITH_AES_256_CCM", "TLS_DHE_PSK_WITH_AES_128_CCM", "TLS_DHE_PSK_WITH_AES_256_CCM", "TLS_PSK_WITH_AES_128_CCM_8", "TLS_PSK_WITH_AES_256_CCM_8", "TLS_PSK_DHE_WITH_AES_128_CCM_8", "TLS_PSK_DHE_WITH_AES_256_CCM_8", "TLS_ECDHE_ECDSA_WITH_AES_128_CCM", "TLS_ECDHE_ECDSA_WITH_AES_256_CCM", "TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8", "TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8", "TLS_ECCPWD_WITH_AES_128_GCM_SHA256", "TLS_ECCPWD_WITH_AES_256_GCM_SHA384", "TLS_ECCPWD_WITH_AES_128_CCM_SHA256", "TLS_ECCPWD_WITH_AES_256_CCM_SHA384", "TLS_SHA256_SHA256", "TLS_SHA384_SHA384", "TLS_GOSTR341112_256_WITH_KUZNYECHIK_CTR_OMAC", "TLS_GOSTR341112_256_WITH_MAGMA_CTR_OMAC", "TLS_GOSTR341112_256_WITH_28147_CNT_IMIT", "TLS_GOSTR341112_256_WITH_KUZNYECHIK_MGM_L", "TLS_GOSTR341112_256_WITH_MAGMA_MGM_L", "TLS_GOSTR341112_256_WITH_KUZNYECHIK_MGM_S", "TLS_GOSTR341112_256_WITH_MAGMA_MGM_S", "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256", "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256", "TLS_DHE_RSA_WITH_CHACHA20_POLY1305_SHA256", "TLS_PSK_WITH_CHACHA20_POLY1305_SHA256", "TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256", "TLS_DHE_PSK_WITH_CHACHA20_POLY1305_SHA256", "TLS_RSA_PSK_WITH_CHACHA20_POLY1305_SHA256", "TLS_ECDHE_PSK_WITH_AES_128_GCM_SHA256", "TLS_ECDHE_PSK_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_PSK_WITH_AES_128_CCM_8_SHA256", "TLS_ECDHE_PSK_WITH_AES_128_CCM_SHA256")
POSSIBLE_DH_PARAMETER_SIZES = ("480", "512", "1024", "2048", "3072", "4096", "6144", "8192")
POSSIBLE_RSA_KEY_SIZES = ("2048", "3072", "4096", "6144", "8192")
POSSIBLE_CERTIFICATE_LIFESPANS = ()

# Categories for each rule
CATEGORIES = ["shall", "should", "should_not", "shall_not"]

# Mapping for subrule categories to human-readable labels
WORD_MAPPING = {
    "shall": "MANDATORY",
    "should": "RECOMMENDED",
    "should_not": "CAUTIONARY",
    "shall_not": "PROHIBITED"
}

# Rules for policy definitions
RULES = [
    # Rule 1 for checking TLS versions
    {
        "rule_name": "TLS VERSION FOR CONNECTION",
        "rule_code": "R01",
        "description": "Checking the TLS Version Used for the Connection",
        "connection_type": "TLS_CONNECTION",
        "connection_field": "TLS_CONNECTION_VERSION",
        "possible_values": POSSIBLE_TLS_VERSIONS,
        "violation_data": {
            "HIGH": {
                "title": "Outdated and Insecure Protocols",
                "description": "SSL v2 and SSL v3 are deprecated and considered highly insecure due to numerous vulnerabilities, including lack of proper encryption and susceptibility to attacks like POODLE. Connections using these protocols risk exposing sensitive data and enabling unauthorized access."
            },
            "MEDIUM": {
                "title": "Legacy Protocols with Weak Security",
                "description": "TLS v1.0 and TLS v1.1 are outdated and no longer considered secure by modern standards. These protocols lack support for strong encryption algorithms and are vulnerable to attacks such as BEAST and downgrade attacks. Migration to TLS v1.2 or higher is strongly recommended."
            },
            "LOW": {
                "title": "Improved but Aging Protocol",
                "description": "While TLS v1.2 is widely used and more secure than older protocols, it lacks the advanced security features of TLS v1.3, such as faster handshakes and stronger default cipher suites. For enhanced security, upgrading to TLS v1.3 is recommended where possible."
            }
        },
        "consequence": "Non-compliance with secure TLS version requirements exposes connections to potential interception, data breaches, and unauthorized access due to known vulnerabilities in outdated protocols.",
        "explanation": "Older TLS versions (SSL v2/v3, TLS 1.0/1.1) lack adequate security measures and are vulnerable to attacks such as POODLE, BEAST, and downgrade attacks, putting encrypted communications at significant risk.",
        "remediation": "Upgrade all systems to support TLS v1.2 or higher, with a preference for TLS v1.3, and disable all outdated protocols to ensure secure and compliant communication.",
        "special_handling": "no"
    },
    # Rule 2 for checking certificate types
    {
        "rule_name": "CERTIFICATE TYPES",
        "rule_code": "R02",
        "description": "Checking the Certificate Types Used for the Connection",
        "connection_type": "TLS_CONNECTION",
        "connection_field": "CERTIFICATE_TYPES",
        "possible_values": POSSIBLE_CERTIFICATE_TYPES,
        "violation_data": {
            "HIGH": {
                "title": "Placeholder for certificate types violation data HIGH title",
                "description": "Placeholder for certificate types violation data HIGH description"
            },
            "MEDIUM": {
                "title": "Placeholder for certificate types violation data MEDIUM title",
                "description": "Placeholder for certificate types violation data MEDIUM description"
            },
            "LOW": {
                "title": "Placeholder for certificate types violation data LOW title",
                "description": "Placeholder for certificate types violation data LOW description"
            }
        },
        "consequence": "Placeholder for certificate types consequence",
        "explanation": "Placeholder for certificate types explanation",
        "remediation": "Placeholder for certificate types remediation",
        "special_handling": "no"
    },
    # Rule 3 for checking certificate curves
    {
        "rule_name": "CERTIFICATE CURVES",
        "rule_code": "R03",
        "description": "Checking the Certificate Curves Used for the Connection",
        "connection_type": "TLS_CONNECTION",
        "connection_field": "CERTIFICATE_CURVES",
        "possible_values": POSSIBLE_TLS_SUPPORTED_GROUPS,
        "violation_data": {
            "HIGH": {
                "title": "Placeholder for certificate curves violation data HIGH title",
                "description": "Placeholder for certificate curves violation data HIGH description"
            },
            "MEDIUM": {
                "title": "Placeholder for certificate curves violation data MEDIUM title",
                "description": "Placeholder for certificate curves violation data MEDIUM description"
            },
            "LOW": {
                "title": "Placeholder for certificate curves violation data LOW title",
                "description": "Placeholder for certificate curves violation data LOW description"
            }
        },
        "consequence": "Placeholder for certificate curves consequence",
        "explanation": "Placeholder for certificate curves explanation",
        "remediation": "Placeholder for certificate curves remediation",
        "special_handling": "no"
    },
    # Rule 4 for checking TLS curves
    {
        "rule_name": "TLS CURVES",
        "rule_code": "R04",
        "description": "Checking the TLS Curves Used for the Connection",
        "connection_type": "TLS_CONNECTION",
        "connection_field": "TLS_CURVES",
        "possible_values": POSSIBLE_TLS_SUPPORTED_GROUPS,
        "violation_data": {
            "HIGH": {
                "title": "Placeholder for TLS curves violation data HIGH title",
                "description": "Placeholder for TLS curves violation data HIGH description"
            },
            "MEDIUM": {
                "title": "Placeholder for TLS curves violation data MEDIUM title",
                "description": "Placeholder for TLS curves violation data MEDIUM description"
            },
            "LOW": {
                "title": "Placeholder for TLS curves violation data LOW title",
                "description": "Placeholder for TLS curves violation data LOW description"
            }
        },
        "consequence": "Placeholder for TLS curves consequence",
        "explanation": "Placeholder for TLS curves explanation",
        "remediation": "Placeholder for TLS curves remediation",
        "special_handling": "no"
    },
    # Rule 5 for checking TLS ciphersuites
    {
        "rule_name": "TLS CIPHERSUITES",
        "rule_code": "R05",
        "description": "Checking the TLS Ciphersuite Used for the Connection",
        "connection_type": "TLS_CONNECTION",
        "connection_field": "TLS_CIPHERSUITE",
        "possible_values": POSSIBLE_TLS_CIPHERSUITES,
        "violation_data": {
            "HIGH": {
                "title": "Placeholder for TLS ciphersuites violation data HIGH title",
                "description": "Placeholder for TLS ciphersuites violation data HIGH description"
            },
            "MEDIUM": {
                "title": "Placeholder for TLS ciphersuites violation data MEDIUM title",
                "description": "Placeholder for TLS ciphersuites violation data MEDIUM description"
            },
            "LOW": {
                "title": "Placeholder for TLS ciphersuites violation data LOW title",
                "description": "Placeholder for TLS ciphersuites violation data LOW description"
            }
        },
        "consequence": "Placeholder for TLS ciphersuites consequence",
        "explanation": "Placeholder for TLS ciphersuites explanation",
        "remediation": "Placeholder for TLS ciphersuites remediation",
        "special_handling": "no"
    },
    # Rule 6 for checking Diffie–Hellman parameter size
    {
        "rule_name": "DH PARAMETER SIZE",
        "rule_code": "R06",
        "description": "Checking the DH Parameter Size Used for the Connection",
        "connection_type": "TLS_CONNECTION",
        "connection_field": "DH_PARAMETER_SIZE",
        "possible_values": POSSIBLE_DH_PARAMETER_SIZES,
        "violation_data": {
            "HIGH": {
                "title": "Placeholder for DH Parameter Size violation data HIGH title",
                "description": "Placeholder for DH Parameter Size violation data HIGH description"
            },
            "MEDIUM": {
                "title": "Placeholder for DH Parameter Size violation data MEDIUM title",
                "description": "Placeholder for DH Parameter Size violation data MEDIUM description"
            },
            "LOW": {
                "title": "Placeholder for DH Parameter Size violation data LOW title",
                "description": "Placeholder for DH Parameter Size violation data LOW description"
            }
        },
        "consequence": "Placeholder for DH Parameter Size consequence",
        "explanation": "Placeholder for DH Parameter Size explanation",
        "remediation": "Placeholder for DH Parameter Size remediation",
        "special_handling": "no"
    },
    # Rule 7 for checking RSA key size
    {
        "rule_name": "RSA KEY SIZE",
        "rule_code": "R07",
        "description": "Checking the RSA Key Size Used for the Connection",
        "connection_type": "TLS_CONNECTION",
        "connection_field": "RSA_KEY_SIZE",
        "possible_values": POSSIBLE_RSA_KEY_SIZES,
        "violation_data": {
            "HIGH": {
                "title": "Placeholder for RSA Key Size violation data HIGH title",
                "description": "Placeholder for RSA Key Size violation data HIGH description"
            },
            "MEDIUM": {
                "title": "Placeholder for RSA Key Size violation data MEDIUM title",
                "description": "Placeholder for RSA Key Size violation data MEDIUM description"
            },
            "LOW": {
                "title": "Placeholder for RSA Key Size violation data LOW title",
                "description": "Placeholder for RSA Key Size violation data LOW description"
            }
        },
        "consequence": "Placeholder for RSA Key Size consequence",
        "explanation": "Placeholder for RSA Key Size explanation",
        "remediation": "Placeholder for RSA Key Size remediation",
        "special_handling": "no"
    },
    # Rule 8 for checking Certificate Lifespan
    {
        "rule_name": "CERTIFICATE LIFESPAN",
        "rule_code": "R08",
        "description": "Checking the Certificate Lifespan Used for the Connection",
        "connection_type": "TLS_CONNECTION",
        "connection_field": "CERTIFICATE_LIFESPAN",
        "possible_values": POSSIBLE_CERTIFICATE_LIFESPANS,
        "violation_data": {
            "HIGH": {
                "title": "Placeholder for Certificate Lifespan violation data HIGH title",
                "description": "Placeholder for Certificate Lifespan violation data HIGH description"
            },
            "MEDIUM": {
                "title": "Placeholder for Certificate Lifespan violation data MEDIUM title",
                "description": "Placeholder for Certificate Lifespan violation data MEDIUM description"
            },
            "LOW": {
                "title": "Placeholder for Certificate Lifespan violation data LOW title",
                "description": "Placeholder for Certificate Lifespan violation data LOW description"
            }
        },
        "consequence": "Placeholder for Certificate Lifespan consequence",
        "explanation": "Placeholder for Certificate Lifespan explanation",
        "remediation": "Placeholder for Certificate Lifespan remediation",
        "special_handling": "no"
    }
]