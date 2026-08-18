namespace PetShop.Orders.Application.Handlers;

using MediatR;
using PetShop.Orders.Application.DTOs;
using PetShop.Orders.Application.Queries;
using PetShop.Orders.Infrastructure.Repositories;

public class GetOrdersHandler : IRequestHandler<GetOrdersQuery, Result<OrderListResponse>>
{
    private readonly IOrderRepository _orderRepository;

    public GetOrdersHandler(IOrderRepository orderRepository)
    {
        _orderRepository = orderRepository;
    }

    public async Task<Result<OrderListResponse>> Handle(GetOrdersQuery request, CancellationToken cancellationToken)
    {
        var orders = await _orderRepository.GetByCustomerIdAsync(request.UserId, request.Page, request.PageSize, cancellationToken);
        var totalCount = await _orderRepository.CountByCustomerIdAsync(request.UserId, cancellationToken);

        return Result<OrderListResponse>.Success(new OrderListResponse(
            orders.Select(MapToResponse),
            totalCount,
            request.Page,
            request.PageSize,
            request.Page < (int)Math.Ceiling((double)totalCount / request.PageSize)
        ));
    }

    private static OrderResponse MapToResponse(PetShop.Orders.Domain.Entities.Order order)
    {
        return new OrderResponse(
            order.Id, order.OrderNumber, order.CustomerId,
            order.Status, order.TotalAmount, order.Currency,
            order.Items.Select(i => new OrderItemResponse(
                i.ProductId, i.ProductName, i.Quantity, i.UnitPrice, i.TotalPrice)),
            order.CreatedAt);
    }
}
