# ASEAN VAT Calculation Guide

## Overview

Value Added Tax (VAT) or Goods and Services Tax (GST) applies to most commercial transactions in ASEAN member states. This guide covers the standard rates, registration thresholds, and calculation methods for each country as of 2026.

## Country-by-Country Rates

### Singapore — GST
- Standard rate: 9% (increased from 8% on 1 January 2024)
- Registration threshold: SGD 1,000,000 annual taxable turnover
- Filing frequency: Quarterly (monthly for large businesses)
- Reverse charge applies to imported services since 1 January 2020
- Digital services: Overseas vendors must register under the Overseas Vendor Registration (OVR) regime if annual B2C supplies to Singapore exceed SGD 100,000

### Malaysia — SST (Sales and Service Tax)
- Sales Tax: 5% or 10% depending on goods category
- Service Tax: 8% (increased from 6% on 1 March 2024)
- Registration threshold: MYR 500,000 annual taxable turnover for service tax
- Digital services: Foreign providers of digital services must register and charge 8% service tax on B2C supplies
- Note: Malaysia replaced GST with SST in September 2018. SST is a single-stage tax, not a multi-stage VAT

### Thailand — VAT
- Standard rate: 7% (statutory rate is 10%, reduced to 7% by royal decree, extended through September 2026)
- Registration threshold: THB 1,800,000 annual revenue
- Filing frequency: Monthly, due by the 15th of the following month
- Zero-rated: Exports of goods, international transport services
- Exempt: Basic foodstuffs, healthcare, education, domestic transport

### Indonesia — PPN (Pajak Pertambahan Nilai)
- Standard rate: 12% (increased from 11% on 1 January 2025)
- Registration threshold: IDR 4,800,000,000 annual gross turnover
- Filing frequency: Monthly
- Luxury goods surcharge (PPnBM): 10% to 200% on top of PPN for luxury items
- Digital services: Foreign providers must appoint a local tax representative or register directly

### Philippines — VAT
- Standard rate: 12%
- Registration threshold: PHP 3,000,000 annual gross sales
- Filing frequency: Quarterly returns, monthly remittance
- Zero-rated: Export sales, services rendered to non-residents
- Exempt: Agricultural products (unprocessed), educational services, health services
- Digital services: Non-resident digital service providers must register for VAT

### Vietnam — VAT (GTGT)
- Standard rate: 10%
- Reduced rate: 5% for essential goods (clean water, medical equipment, educational materials, agricultural inputs)
- Temporary reduction: 8% on goods/services normally subject to 10% (periodic government stimulus, check current status)
- Registration: All business entities must register; no minimum threshold
- Filing frequency: Monthly (quarterly for businesses with annual revenue under VND 50 billion)
- Foreign contractor tax (FCT) applies to non-resident suppliers: 5% VAT component

### Cambodia — VAT
- Standard rate: 10%
- Registration threshold: KHR 250,000,000 (approximately USD 62,500) annual turnover
- Filing frequency: Monthly, due by the 20th of the following month
- Zero-rated: Exports
- Exempt: Public postal services, medical and dental services, public transport, insurance

### Myanmar — Commercial Tax
- Standard rate: 5% on most goods and services
- Special rates: 8% on selected goods (soft drinks, alcohol, tobacco products range from 25% to 80%)
- Registration: Applies to businesses with annual turnover exceeding MMK 50,000,000
- Note: Myanmar uses a commercial tax system rather than a traditional VAT

### Laos — VAT
- Standard rate: 7%
- Registration threshold: LAK 400,000,000 annual turnover
- Filing frequency: Monthly
- Zero-rated: Exports, international transport
- Exempt: Agricultural products, medical services, education

### Brunei
- No VAT or GST. Brunei does not impose any broad-based consumption tax.

## Calculation Method

### Standard VAT Calculation

```
VAT Amount = Taxable Base × VAT Rate
Total Price = Taxable Base + VAT Amount
```

Example (Thailand, 7%):
- Product price: THB 10,000
- VAT: THB 10,000 × 0.07 = THB 700
- Total: THB 10,700

### Extracting VAT from a VAT-Inclusive Price

```
VAT Amount = Inclusive Price × (VAT Rate / (1 + VAT Rate))
Net Price = Inclusive Price - VAT Amount
```

Example (Indonesia, 12%):
- Inclusive price: IDR 1,120,000
- VAT: IDR 1,120,000 × (0.12 / 1.12) = IDR 120,000
- Net price: IDR 1,000,000

### Cross-Border B2B Transactions

For B2B services between ASEAN countries:
1. Determine the place of supply (generally where the recipient is located)
2. Check if a reverse charge mechanism applies (Singapore, Thailand, Indonesia have reverse charge rules)
3. If reverse charge applies, the recipient self-assesses VAT on the import and claims input credit simultaneously (net zero effect for fully taxable businesses)
4. If no reverse charge, the supplier may need to register in the destination country

### Digital Services

Most ASEAN countries now require foreign digital service providers to register and collect VAT/GST:
- Singapore: OVR regime, 9% GST on B2C digital services
- Indonesia: PMSE regime, 12% PPN on digital services
- Thailand: e-Service VAT, 7% on electronic services to non-VAT-registered recipients
- Malaysia: 8% service tax on digital services
- Philippines: 12% VAT on digital services (effective 2025)
- Vietnam: Foreign contractor tax applies (5% VAT + 5% CIT = 10% total)

## Input Tax Credit

In countries with a multi-stage VAT (all except Malaysia and Myanmar), businesses can claim input tax credits:

```
Net VAT Payable = Output VAT (collected from customers) - Input VAT (paid to suppliers)
```

Requirements for claiming input credits:
- Valid tax invoice from the supplier
- Goods or services used for taxable business purposes
- Claim filed within the statutory time limit (varies by country, typically 6-12 months)

## Common Pitfalls

1. Applying the wrong rate after a rate change (e.g., Indonesia's increase to 12% in 2025)
2. Failing to register for VAT when the threshold is met — penalties apply retroactively
3. Not accounting for reverse charge on imported services (especially in Singapore and Thailand)
4. Treating Malaysia's SST like a VAT — SST has no input credit mechanism
5. Ignoring digital services registration requirements when selling SaaS products into ASEAN markets
6. Using outdated temporary rates (e.g., Vietnam's periodic 8% reduction may expire)
