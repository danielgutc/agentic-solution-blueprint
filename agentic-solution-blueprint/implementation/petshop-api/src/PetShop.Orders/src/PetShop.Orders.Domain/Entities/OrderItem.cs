namespace PetShop.Orders.Domain.Entities;

public class OrderItem : PetShop.Shared.Domain.Entity<Guid>
{
    public Guid OrderId { get; private set; }
    public Guid ProductId { get; private set; }
    public string ProductName { get; private set; }
    public decimal UnitPrice { get; private set; }
    public int Quantity { get; private set; }

    public decimal TotalPrice => UnitPrice * Quantity;

    public OrderItem()
    {
        ProductName = string.Empty;
        UnitPrice = 0m;
        Quantity = 0;
    }

    public OrderItem(Guid id, Guid orderId, Guid productId, string productName, decimal unitPrice, int quantity)
    {
        Id = id;
        OrderId = orderId;
        ProductId = productId;
        ProductName = productName;
        UnitPrice = unitPrice;
        Quantity = quantity;
    }
}
