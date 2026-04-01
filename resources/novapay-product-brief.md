# NovaPay — Product Brief

## What It Is

NovaPay is a payment processing platform for mid-market and enterprise retailers. It handles in-store, online, and mobile payments through a single unified API — one integration, one dashboard, one settlement file. Think of it as what happens when you take the simplicity of Stripe and combine it with the in-store capabilities of a traditional processor, then add ML-powered fraud detection on top.

## Who It's For

Retailers processing $50K to $20M+ per month who are tired of managing separate processors for POS and e-commerce. The sweet spot is multi-location retailers with both physical stores and an online channel.

## Core Features

**Unified Gateway** — Card-present (POS terminals), card-not-present (online), and mobile wallets (Apple Pay, Google Pay) all flow through one platform. Merchants reconcile once instead of juggling multiple processors.

**Interchange-Plus Pricing** — Merchants pay the card network's actual interchange fee plus a transparent NovaPay markup. No bundled flat rates hiding margin. This saves high-volume merchants 15-30% compared to flat-rate processors like Stripe or Square.

**ShieldAI Fraud Detection** — ML engine trained on 2B+ transactions. Assigns a 0-100 risk score to every transaction in real time. Merchants configure auto-decline thresholds, velocity rules, and geo-blocking. Reduces fraud losses by an average of 68%.

**Tokenization & Vault** — Card data is tokenized at entry. PCI DSS Level 1 certified vault stores tokens, not raw numbers. Cross-channel recognition lets a customer who pays online be identified in-store.

**Real-Time Analytics** — Dashboard with live transaction monitoring, revenue heatmaps, chargeback tracking, and fraud scoring. Refreshes every 30 seconds. Historical data exportable via CSV or Reporting API.

## Integration Options

| Path | Effort | PCI Requirement | Best For |
|---|---|---|---|
| Hosted Checkout | 1-2 days | None (NovaPay handles it) | Quick launch, no dev resources |
| Drop-In SDK | 1-2 weeks | SAQ-A (20-question form) | Most merchants — card data never touches their servers |
| Server-to-Server API | 4-6 weeks | Full PCI DSS Level 1 | Enterprise with dedicated security teams |

## Payment Methods

Cards (Visa, Mastercard, Amex, Discover), digital wallets (Apple Pay, Google Pay, Samsung Pay), ACH direct debit (US), and Buy Now Pay Later (Affirm, Klarna).

## Pricing at a Glance

| Channel | NovaPay Markup |
|---|---|
| In-store (POS) | Interchange + 0.20% + $0.08 |
| Online | Interchange + 0.30% + $0.12 |
| ACH | 0.80% (capped at $5) |

Three plans: Starter (free, up to $50K/mo), Growth ($149/mo, up to $500K/mo), Enterprise (custom, no cap). Volume discounts kick in at $1M/month.

No setup fees, no annual fees, no PCI compliance fees, no early termination fees.

## Security

PCI DSS Level 1 certified. SOC 2 Type II audited. All data encrypted with AES-256 at rest, TLS 1.3 in transit. Runs on AWS with active-active across two regions. 99.99% uptime SLA on Enterprise.

## What's Coming

Canada and UK expansion targeted for Q3 2026 (August launch for Canada). Multi-currency settlement is on the roadmap but not available today. Currently US-only, USD-only.
