namespace PetShop.Orders.Domain.Events;

public record OrderPlacedEvent(
    Guid OrderId,
    string OrderNumber,
    Guid CustomerId,
    decimal TotalAmount,
    IEnumerable<OrderItemEvent> Items
);

public record OrderItemEvent(
    Guid ProductId,
    string ProductName,
    int Quantity,
    decimal UnitPrice
);

public record OrderConfirmedEvent(
    Guid OrderId,
    string OrderNumber,
    Guid CustomerId
);

public record OrderShippedEvent(
    Guid OrderId,
    string OrderNumber,
    string TrackingNumber
);
