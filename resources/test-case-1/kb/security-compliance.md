# NovaPay Security & Compliance

## Compliance Certifications

NovaPay holds the following certifications:
- **PCI DSS Level 1** — The highest level of PCI compliance. Validated annually by a Qualified Security Assessor (QSA). Our most recent Report on Compliance (ROC) was issued in January 2026.
- **SOC 2 Type II** — Covers security, availability, and confidentiality trust principles. Our latest audit report covers the 12-month period ending December 2025.
- **GDPR** — While NovaPay currently operates in the US only, our data handling practices comply with GDPR requirements in preparation for international expansion.

## Data Encryption

- **In transit**: All API communication uses TLS 1.3. Older TLS versions (1.0, 1.1) are rejected. TLS 1.2 is accepted but 1.3 is preferred.
- **At rest**: All card data stored in the vault is encrypted with AES-256. Encryption keys are managed via AWS KMS with automatic annual rotation.
- **Tokenization**: Raw card numbers are replaced with non-reversible tokens at the point of entry. Tokens cannot be used outside the NovaPay ecosystem.

## Infrastructure Security

NovaPay runs on AWS in the us-east-1 (Virginia) and us-west-2 (Oregon) regions with active-active failover. Key infrastructure controls:
- All compute runs in private VPC subnets with no direct internet access
- Database access requires IAM authentication plus network-level restrictions
- DDoS protection via AWS Shield Advanced
- Web Application Firewall (WAF) on all API endpoints
- Penetration testing conducted quarterly by an independent firm (NCC Group)

## Fraud Prevention (ShieldAI)

ShieldAI is NovaPay's ML-based fraud detection engine. It evaluates every transaction in real time and assigns a risk score from 0 (low risk) to 100 (high risk). Merchants can configure:
- **Auto-decline threshold**: Transactions scoring above this value are automatically declined (default: 85)
- **Review threshold**: Transactions between this value and the auto-decline threshold are flagged for manual review (default: 60)
- **Velocity rules**: Limit the number of transactions per card, per IP, or per device within a time window
- **Geo-blocking**: Block transactions from specific countries or regions

ShieldAI models are retrained monthly on anonymized transaction data from across the NovaPay network.

## Incident Response

NovaPay maintains a 24/7 Security Operations Center (SOC). Incident response SLAs:
- Critical (data breach, system compromise): Response within 15 minutes, customer notification within 4 hours
- High (service degradation, suspicious activity): Response within 1 hour
- Medium (vulnerability discovered, policy violation): Response within 4 hours

## Data Retention

- Transaction records: Retained for 7 years (regulatory requirement)
- API request logs: Retained for 90 days
- Tokenized card data: Retained until merchant requests deletion or token expires (configurable, default: no expiry)
