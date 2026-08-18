namespace PetShop.Orders.Application.DTOs;

public record PlaceOrderRequest(
    Guid CartId
);

public record UpdateOrderStatusRequest(
    OrderStatus Status
);

public record OrderResponse(
    Guid Id,
    string OrderNumber,
    Guid CustomerId,
    OrderStatus Status,
    decimal TotalAmount,
    string Currency,
    IEnumerable<OrderItemResponse> Items,
    DateTime CreatedAt
);

public record OrderItemResponse(
    Guid ProductId,
    string ProductName,
    int Quantity,
    decimal UnitPrice,
    decimal TotalPrice
);

public record OrderListResponse(
    IEnumerable<OrderResponse> Items,
    int TotalCount,
    int Page,
    int PageSize,
    bool HasNextPage
);
