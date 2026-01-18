# 🅿️ Parking Lot Management System

A complete parking lot management system built with Python following SOLID principles and design patterns.

## 🚀 Features

### ✅ Ticket Management
- Vehicle entry with ticket issuance
- Automatic slot assignment using strategy pattern
- Multiple vehicle type support (Car, Bike, Truck, Bus)
- Real-time capacity tracking
- Gate management with entry/exit gates

### ✅ Billing & Payment
- Automated bill generation on exit
- Flexible pricing strategies (Hourly, Fixed+Hourly)
- Multiple payment modes (Cash, Card, Online, UPI)
- Partial payments support
- Bill status tracking (PENDING, PARTIALLY_PAID, PAID)

### ✅ Resource Management
- Dynamic slot allocation and deallocation
- Parking lot capacity management
- Multi-floor parking support
- Slot status tracking (EMPTY, FILLED, RESERVED, BLOCKED)

### ✅ Design Patterns Implemented
- **Strategy Pattern**: Slot assignment & Pricing strategies
- **Repository Pattern**: Data access abstraction
- **Factory Pattern**: Strategy creation
- **DTO Pattern**: Clean data transfer
- **MVC Pattern**: Controller-Service-Repo architecture
- **Observer Pattern**: (Optional - for future notifications)

## 📁 Project Structure
parking-lot-management-system/
├── ParkingLot/
│   ├── controller/
│   ├── service/
│   ├── repo/
│   ├── dtos/
│   ├── strgy/
│   ├── models/
│   └── main.py
├── README.md
├── .gitignore
└── requirements.txt (optional)
 
```bash
# Clone the repository
git clone https://github.com/yourusername/parking-lot-management-system.git

# Navigate to project directory
cd parking-lot-management-system

# Run the main program
python ParkingLot/main.py
