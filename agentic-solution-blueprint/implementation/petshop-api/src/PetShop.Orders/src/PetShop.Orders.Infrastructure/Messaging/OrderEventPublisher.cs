namespace PetShop.Orders.Infrastructure.Messaging;

using Microsoft.Extensions.Logging;
using PetShop.Orders.Domain.Events;
using RabbitMQ.Client;
using System.Text;
using System.Text.Json;

public class OrderEventPublisher : IOrderEventPublisher
{
    private readonly IConfiguration _configuration;
    private readonly ILogger<OrderEventPublisher> _logger;

    public OrderEventPublisher(IConfiguration configuration, ILogger<OrderEventPublisher> logger)
    {
        _configuration = configuration;
        _logger = logger;
    }

    public async Task PublishOrderPlacedAsync(OrderPlacedEvent @event, CancellationToken cancellationToken = default)
    {
        await PublishAsync("order.events", "order.placed", @event, cancellationToken);
    }

    public async Task PublishOrderConfirmedAsync(OrderConfirmedEvent @event, CancellationToken cancellationToken = default)
    {
        await PublishAsync("order.events", "order.confirmed", @event, cancellationToken);
    }

    public async Task PublishOrderShippedAsync(OrderShippedEvent @event, CancellationToken cancellationToken = default)
    {
        await PublishAsync("order.events", "order.shipped", @event, cancellationToken);
    }

    private async Task PublishAsync(string exchange, string routingKey, object message, CancellationToken cancellationToken)
    {
        var factory = new ConnectionFactory()
        {
            HostName = _configuration["RabbitMQ:HostName"] ?? "localhost",
            UserName = _configuration["RabbitMQ:UserName"] ?? "guest",
            Password = _configuration["RabbitMQ:Password"] ?? "guest"
        };

        using var connection = await factory.CreateConnectionAsync(cancellationToken);
        using var channel = await connection.CreateChannelAsync(cancellationToken);

        await channel.ExchangeDeclareAsync(exchange, ExchangeType.Fanout, durable: true);

        var body = Encoding.UTF8.GetBytes(JsonSerializer.Serialize(message));
        await channel.BasicPublishAsync(exchange, routingKey, body: body);

        _logger.LogInformation("Published {EventType} to exchange {Exchange}", routingKey, exchange);
    }
}
