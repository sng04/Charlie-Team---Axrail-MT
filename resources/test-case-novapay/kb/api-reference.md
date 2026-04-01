# NovaPay API Reference

## Base URL
```
Production: https://api.novapay.com/v1
Sandbox:    https://sandbox.novapay.com/v1
```

## Authentication
All API requests require an API key passed in the `Authorization` header:
```
Authorization: Bearer sk_live_xxxxxxxxxxxx
```
Sandbox keys use the prefix `sk_test_`. Live keys use `sk_live_`. Keys are generated in the NovaPay Dashboard under Settings > API Keys.

## Payments API

### Create a Payment
```
POST /payments
```
Creates a new payment intent. The payment is authorized but not captured until you call the capture endpoint (or enable auto-capture).

Request body:
- `amount` (integer, required): Amount in cents. Example: 1999 = $19.99
- `currency` (string, required): Three-letter ISO currency code. Currently only "usd" is supported.
- `payment_method` (string, required): Token ID returned by the Drop-In SDK or a stored token from the Vault.
- `description` (string, optional): Internal description for the transaction.
- `metadata` (object, optional): Key-value pairs for merchant-defined data. Up to 20 keys, 500 chars per value.
- `capture` (boolean, optional): If true, payment is captured immediately. Default: false.
- `idempotency_key` (string, optional): Unique key to prevent duplicate charges. Recommended for all production requests.

Response:
- `id`: Payment ID (e.g., `pay_abc123`)
- `status`: `authorized`, `captured`, `failed`, `refunded`
- `amount`, `currency`, `created_at`

### Capture a Payment
```
POST /payments/{paymentId}/capture
```
Captures a previously authorized payment. Must be called within 7 days of authorization.

### Refund a Payment
```
POST /payments/{paymentId}/refund
```
Issues a full or partial refund. Partial refunds specify an `amount` field.

## Webhooks

NovaPay sends real-time event notifications to a URL you configure in the Dashboard. Events include:
- `payment.authorized` — Payment successfully authorized
- `payment.captured` — Payment captured
- `payment.failed` — Payment failed (includes `failure_reason`)
- `payment.refunded` — Refund processed
- `chargeback.created` — Chargeback filed by cardholder
- `payout.completed` — Funds deposited to merchant bank account

Webhook payloads are signed with HMAC-SHA256. Verify the `X-NovaPay-Signature` header before processing.

## Rate Limits

- Sandbox: 100 requests/minute
- Production: 1,000 requests/minute (Starter/Growth) or 10,000 requests/minute (Enterprise)

## SDKs

Official SDKs are available for:
- JavaScript/TypeScript (npm: `@novapay/js`)
- Python (`pip install novapay`)
- Ruby (`gem install novapay`)
- PHP (Composer: `novapay/novapay-php`)
- Java (Maven: `com.novapay:novapay-java`)

All SDKs handle tokenization, retries, and webhook signature verification.

## Onboarding Timeline

Typical integration timeline:
- Hosted Checkout: 1-2 days
- Drop-In SDK: 1-2 weeks
- Server-to-Server API: 4-6 weeks (includes PCI audit)

Sandbox access is instant. Production credentials are issued after identity verification (KYB), which takes 2-3 business days.
