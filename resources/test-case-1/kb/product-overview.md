# NovaPay Product Overview

## What is NovaPay?

NovaPay is a cloud-native payment processing platform built for mid-market and enterprise retailers. It handles in-store, online, and mobile payments through a single unified API. NovaPay processes transactions in under 200 milliseconds and maintains 99.99% uptime across all payment channels.

## Core Capabilities

### Unified Payment Gateway
NovaPay consolidates card-present (POS terminal), card-not-present (ecommerce), and mobile wallet transactions into one platform. Merchants receive a single dashboard, a single settlement file, and a single integration to maintain. Supported card networks include Visa, Mastercard, American Express, and Discover.

### Tokenization and Vault
All card data is tokenized at the point of entry. NovaPay's PCI DSS Level 1 certified vault stores tokens, not raw card numbers. Tokens can be reused for recurring billing, one-click checkout, and cross-channel recognition (a customer who pays online can be recognized in-store).

### Real-Time Analytics Dashboard
The merchant dashboard provides real-time transaction monitoring, hourly revenue heatmaps, chargeback tracking, and fraud scoring. Data refreshes every 30 seconds. Historical reports can be exported as CSV or accessed via the Reporting API.

### Fraud Detection Engine
NovaPay includes a built-in fraud detection engine called ShieldAI. It uses machine learning models trained on over 2 billion transactions to assign a risk score (0-100) to every transaction. Merchants can configure auto-decline thresholds, velocity rules, and geo-blocking policies. ShieldAI reduces fraud losses by an average of 68% compared to rule-based systems.

## Integration Options

NovaPay offers three integration paths:

1. **Hosted Checkout** — A pre-built, PCI-compliant payment form hosted on NovaPay's domain. Requires zero frontend development. Merchants redirect customers to the checkout page and receive a webhook on completion.

2. **Drop-In SDK** — JavaScript and mobile SDKs (iOS, Android) that render a payment form inside the merchant's UI. Card data is sent directly to NovaPay's servers — it never touches the merchant's backend. Requires PCI SAQ-A compliance only.

3. **Server-to-Server API** — Full control over the payment flow. The merchant collects card data, encrypts it with NovaPay's public key, and sends it to the Payments API. Requires PCI DSS Level 1 compliance. Recommended only for enterprise merchants with dedicated security teams.

## Supported Payment Methods

- Credit and debit cards (Visa, Mastercard, Amex, Discover)
- Digital wallets (Apple Pay, Google Pay, Samsung Pay)
- ACH direct debit (US only)
- Buy Now Pay Later via Affirm and Klarna integrations

## Settlement and Payouts

Standard settlement is T+1 (next business day) for card transactions and T+2 for ACH. NovaPay supports same-day settlement for an additional 0.15% per transaction. Payouts are sent via ACH to the merchant's designated bank account. International payouts are not currently supported — merchants must have a US-domiciled bank account.

## Platform Availability

NovaPay is available in the United States. Expansion to Canada and the United Kingdom is planned for Q3 2026. NovaPay does not currently support multi-currency processing — all transactions are settled in USD.
