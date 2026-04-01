# USD to ASEAN Currency Conversion Guide

## Overview

Reference rates for converting USD to ASEAN currencies. Rates are indicative mid-market rates as of Q1 2026. Actual transaction rates will vary based on the payment processor's FX markup, settlement timing, and corridor.

## Current Exchange Rates (Indicative)

| Currency | Code | Rate (1 USD =) | Common Denomination |
|---|---|---|---|
| Malaysian Ringgit | MYR | 4.42 | Sen (1/100) |
| Singapore Dollar | SGD | 1.34 | Cent (1/100) |
| Thai Baht | THB | 34.50 | Satang (1/100) |
| Indonesian Rupiah | IDR | 15,850 | — |
| Philippine Peso | PHP | 56.20 | Centavo (1/100) |
| Vietnamese Dong | VND | 25,450 | — |
| Cambodian Riel | KHR | 4,100 | — |
| Myanmar Kyat | MMK | 2,100 | — |
| Lao Kip | LAK | 21,800 | — |
| Brunei Dollar | BND | 1.34 | Cent (1/100, pegged to SGD) |

## Quick Conversion Examples

### $10,000 USD equivalent in ASEAN currencies

| Currency | Amount | Formatted |
|---|---|---|
| MYR | 44,200 | RM 44,200.00 |
| SGD | 13,400 | S$ 13,400.00 |
| THB | 345,000 | ฿ 345,000.00 |
| IDR | 158,500,000 | Rp 158.500.000 |
| PHP | 562,000 | ₱ 562,000.00 |
| VND | 254,500,000 | ₫ 254.500.000 |

### NovaPay Pricing in Local Currency

NovaPay's interchange-plus markup converted to local equivalents:

**In-store (POS): Interchange + 0.20% + $0.08**

| Market | Per-transaction fee equivalent |
|---|---|
| Malaysia | RM 0.35 |
| Singapore | S$ 0.11 |
| Thailand | ฿ 2.76 |
| Indonesia | Rp 1,268 |
| Philippines | ₱ 4.50 |

**Online: Interchange + 0.30% + $0.12**

| Market | Per-transaction fee equivalent |
|---|---|
| Malaysia | RM 0.53 |
| Singapore | S$ 0.16 |
| Thailand | ฿ 4.14 |
| Indonesia | Rp 1,902 |
| Philippines | ₱ 6.74 |

## FX Considerations for SEA Expansion

### Settlement Currency

NovaPay currently settles in USD only. For SEA merchants:
- Merchants accepting local currency will need FX conversion at settlement
- Typical FX markup from payment processors: 1.0-2.5% above mid-market
- NovaPay's planned multi-currency settlement (roadmap) would eliminate this

### Dual Pricing

Some SEA markets allow dual pricing (showing both USD and local currency). This is common in:
- Singapore (widely accepted)
- Thailand (tourist areas)
- Cambodia (USD widely circulated alongside KHR)

Not recommended in Malaysia, Indonesia, or Philippines where local currency pricing is expected.

### Regulatory Notes

- **Malaysia**: Bank Negara Malaysia requires all domestic transactions in MYR
- **Indonesia**: Bank Indonesia mandates IDR for all domestic transactions since 2015
- **Thailand**: BOT requires THB for domestic, but cross-border can be in USD
- **Singapore**: No currency restrictions, multi-currency common
- **Philippines**: BSP allows USD accounts but domestic retail must price in PHP

## Volume-Based FX Optimization

For merchants processing over $100K/month equivalent:
- Negotiate dedicated FX rates with the acquiring bank
- Consider treasury hedging for predictable monthly volumes
- Batch settlements to reduce per-transaction FX costs
- Target settlement windows when USD/local spreads are tightest (typically 9-11 AM local time)
