# Issue 01: HTTP 500 Error on POST /users When Phone Number is Empty

**Component:** `sample_repository/app.py`  
**Endpoint:** `POST /users`  
**Severity:** High (Crash / 500 Internal Server Error)  
**Status:** Open  

---

## 🐞 Problem Description

When an external client submits a user creation payload with an empty string or whitespace-only value for the `phone` field, the API endpoint crashes with an unhandled exception:

```text
ValueError: Phone number must contain exactly 10 digits, got ''
```

Because FastAPI does not catch arbitrary `ValueError` exceptions raised inside custom formatting helper functions, the server responds with:
- **HTTP Status:** `500 Internal Server Error`
- **Response Body:** `Internal Server Error`

---

## 📋 Steps to Reproduce

1. Start the sample FastAPI application:
   ```bash
   uvicorn sample_repository.app:app --port 8000
   ```
2. Send a POST request with an empty phone field:
   ```bash
   curl -X POST http://localhost:8000/users \
     -H "Content-Type: application/json" \
     -d '{"name": "Jane Doe", "email": "jane@example.com", "phone": ""}'
   ```
3. Observe the response code: `500 Internal Server Error`.

---

## 🎯 Expected Behavior

- The API should validate the `phone` field prior to attempting formatting or parsing.
- If the phone number is missing, empty, or whitespace-only, the API should reject the request gracefully with:
  - **HTTP Status:** `400 Bad Request`
  - **Response Body:** `{"detail": "Phone number cannot be empty"}` (or equivalent descriptive validation message)

---

## 🧪 Acceptance Criteria

1. Running `pytest sample_repository/test_app.py -k test_create_user_with_empty_phone_should_return_400` passes with HTTP 400.
2. Existing valid user creation tests (`test_create_valid_user`) continue to pass without regression.
