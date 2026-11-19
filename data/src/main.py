# Entry point
from sqlalchemy.orm import Session
from infrastructure.database import SessionLocal

def main():
    db: Session = SessionLocal()
    print("Skeleton compiles successfully")

if __name__ == "__main__":
    main()