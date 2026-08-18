namespace PetShop.Orders.Domain.Entities;

public enum PaymentStatus
{
    Pending,
    Authorized,
    Captured,
    Failed,
    Refunded
}
