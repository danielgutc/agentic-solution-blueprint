namespace PetShop.Orders.Domain.Entities;

public class Payment : PetShop.Shared.Domain.Entity<Guid>
{
    public Guid OrderId { get; private set; }
    public string? PaymentIntentId { get; private set; }
    public PaymentStatus Status { get; private set; }
    public decimal Amount { get; private set; }
    public string Currency { get; private set; }

    public Payment()
    {
        Status = PaymentStatus.Pending;
        Currency = "USD";
    }

    public Payment(Guid id, Guid orderId, decimal amount, string? paymentIntentId = null)
    {
        Id = id;
        OrderId = orderId;
        Amount = amount;
        PaymentIntentId = paymentIntentId;
        Status = PaymentStatus.Pending;
        Currency = "USD";
    }

    public void Authorize(string paymentIntentId)
    {
        PaymentIntentId = paymentIntentId;
        Status = PaymentStatus.Authorized;
        MarkUpdated();
    }

    public void Capture()
    {
        if (Status != PaymentStatus.Authorized)
            throw new PetShop.Shared.Domain.DomainException("Payment must be authorized before capture.");
        Status = PaymentStatus.Captured;
        MarkUpdated();
    }

    public void Fail()
    {
        Status = PaymentStatus.Failed;
        MarkUpdated();
    }
}
