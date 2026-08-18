namespace PetShop.Orders.Domain.Entities;

public class Order : PetShop.Shared.Domain.Entity<Guid>
{
    public string OrderNumber { get; private set; }
    public Guid CustomerId { get; private set; }
    public OrderStatus Status { get; private set; }
    public decimal TotalAmount { get; private set; }
    public string Currency { get; private set; }
    public string? ShippingAddress { get; private set; }
    public string? BillingAddress { get; private set; }

    private readonly List<OrderItem> _items = new();
    public IReadOnlyCollection<OrderItem> Items => _items.AsReadOnly();

    public Order()
    {
        OrderNumber = string.Empty;
        Status = OrderStatus.Pending;
        TotalAmount = 0m;
        Currency = "USD";
    }

    public Order(Guid id, string orderNumber, Guid customerId, decimal totalAmount, string currency = "USD")
    {
        Id = id;
        OrderNumber = orderNumber;
        CustomerId = customerId;
        Status = OrderStatus.Pending;
        TotalAmount = totalAmount;
        Currency = currency;
    }

    public void AddItem(Guid productId, string productName, decimal unitPrice, int quantity)
    {
        var item = new OrderItem(Guid.NewGuid(), Id, productId, productName, unitPrice, quantity);
        _items.Add(item);
        TotalAmount = _items.Sum(i => i.TotalPrice);
        MarkUpdated();
    }

    public void UpdateStatus(OrderStatus status)
    {
        // Validate transition
        if (!IsValidTransition(Status, status))
            throw new PetShop.Shared.Domain.DomainException($"Invalid status transition from {Status} to {status}.");

        Status = status;
        MarkUpdated();
    }

    private static bool IsValidTransition(OrderStatus from, OrderStatus to)
    {
        return (from, to) switch
        {
            (OrderStatus.Pending, OrderStatus.Processing) => true,
            (OrderStatus.Pending, OrderStatus.Cancelled) => true,
            (OrderStatus.Processing, OrderStatus.Shipped) => true,
            (OrderStatus.Processing, OrderStatus.Cancelled) => true,
            (OrderStatus.Shipped, OrderStatus.Delivered) => true,
            (_, OrderStatus.Cancelled) => true,
            _ => false
        };
    }

    public bool IsPending => Status == OrderStatus.Pending;
    public bool IsCompleted => Status == OrderStatus.Delivered;
}
