# 🅿️ Parking Lot Management System (LLD)

A complete **Parking Lot Management System** built using **Python**, following **SOLID principles**, **clean architecture**, and **industry-standard design patterns**.
This project is designed to be **LLD interview-ready** for product-based companies.

---

## 🚀 Features

### ✅ Ticket Management

* Vehicle entry with ticket issuance
* Automatic slot assignment using **Strategy Pattern**
* Multiple vehicle types supported (Car, Bike, Truck, Bus)
* Real-time parking capacity tracking
* Entry and Exit gate management

---

### ✅ Billing & Payment

* Automated bill generation at exit
* Flexible pricing strategies:

  * Hourly Pricing
  * Fixed + Hourly Pricing
* Multiple payment modes:

  * Cash
  * Card
  * UPI / Online
* Partial payments supported
* Bill status tracking:

  * `PENDING`
  * `PARTIALLY_PAID`
  * `PAID`

---

### ✅ Resource Management

* Dynamic slot allocation and deallocation
* Parking lot capacity management
* Multi-floor parking support
* Slot status tracking:

  * `EMPTY`
  * `FILLED`
  * `RESERVED`
  * `BLOCKED`

---

## 🧩 Design Patterns Implemented

| Pattern                         | Usage                             |
| ------------------------------- | --------------------------------- |
| **Strategy Pattern**            | Slot assignment & Pricing logic   |
| **Factory Pattern**             | Strategy object creation          |
| **Repository Pattern**          | Data access abstraction           |
| **DTO Pattern**                 | Clean data transfer               |
| **MVC / Layered Architecture**  | Controller → Service → Repository |
| **Observer Pattern (Optional)** | Notifications (future scope)      |

📌 **Why patterns?**
To avoid `if-else` explosion, improve extensibility, and make the system interview-friendly.

---

## 📁 Project Structure

```
parking-lot-management-system/
│
├── ParkingLot/
│   ├── controller/        # Handles user requests
│   ├── service/           # Business logic
│   ├── repo/              # Data access layer
│   ├── dtos/              # Data Transfer Objects
│   ├── strgy/             # Slot & Pricing strategies
│   ├── models/            # Core domain models
│   └── main.py            # Application entry point
│
├── README.md
├── .gitignore
└── requirements.txt       # (optional)
```

---

## 🔁 High-Level Flow (Ticket Issuance)

1. Vehicle arrives at **Entry Gate**
2. `TicketController` receives the request
3. `TicketService`:

   * Validates gate
   * Fetches or creates vehicle
   * Requests slot from Slot Strategy
   * Generates ticket
4. Ticket is stored and returned to user

---

## 📐 UML – Class Diagram (Text-Based)

```text
+------------------+
|     Vehicle      |
+------------------+
| number           |
| type             |
+------------------+

+------------------+
|   ParkingSlot    |
+------------------+
| slot_id          |
| status           |
| vehicle_type     |
+------------------+

+------------------+
|      Ticket      |
+------------------+
| id               |
| entry_time       |
| vehicle          |
| parking_slot     |
| gate             |
+------------------+

TicketService --> SlotFindingStrategy
TicketService --> PricingStrategy
TicketService --> TicketRepository
```

---

## 📐 UML – Strategy Pattern (Slot Allocation)

```text
+--------------------------+
| SlotFindingStrategy      |
+--------------------------+
| find_slot()              |
+--------------------------+
            ▲
            |
+------------------------------+
| RandomSlotFindingStrategy    |
+------------------------------+
```

---

## 📐 UML – Sequence Diagram (Vehicle Entry)

```text
Vehicle
   |
   v
TicketController
   |
   v
TicketService
   |
   v
SlotStrategyFactory
   |
   v
SlotFindingStrategy
   |
   v
ParkingSlot
```

---

## 💰 Pricing Strategy UML

```text
+--------------------+
| PricingStrategy    |
+--------------------+
| calculate_amount() |
+--------------------+
        ▲
        |
+---------------------------+
| HourlyPricingStrategy     |
+---------------------------+
```

---

## ▶️ How to Run

```bash
# Clone repository
git clone https://github.com/yourusername/parking-lot-management-system.git

# Navigate to project
cd parking-lot-management-system

# Run application
python ParkingLot/main.py
```

---

## 🧪 Extensibility Examples

* Add new vehicle type → update `VehicleType` enum
* Add new pricing logic → implement `PricingStrategy`
* Add nearest-slot logic → new `SlotFindingStrategy`
* Add notifications → Observer Pattern

---

## 🎤 Interview Talking Points

* “I used Strategy + Factory to keep business rules open for extension.”
* “Repositories isolate persistence logic.”
* “Layered architecture improves maintainability and testability.”
* “Design strictly follows SOLID principles.”

---

## 📈 Future Enhancements

* Exit gate controller
* REST API layer (FastAPI)
* Persistent DB storage
* Real-time slot dashboard
* Notification service

---

## 👩‍💻 Author

**Karthika U**
Parking Lot Management System – LLD Interview Ready
