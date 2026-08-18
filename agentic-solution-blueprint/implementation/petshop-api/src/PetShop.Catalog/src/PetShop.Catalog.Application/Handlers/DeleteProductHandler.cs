namespace PetShop.Catalog.Application.Handlers;

using MediatR;
using PetShop.Catalog.Application.Commands;
using PetShop.Catalog.Domain.Entities;
using PetShop.Catalog.Infrastructure.Repositories;

public class DeleteProductHandler : IRequestHandler<DeleteProductCommand, Result>
{
    private readonly IProductRepository _productRepository;
    private readonly IProductCacheService _cacheService;

    public DeleteProductHandler(
        IProductRepository productRepository,
        IProductCacheService cacheService)
    {
        _productRepository = productRepository;
        _cacheService = cacheService;
    }

    public async Task<Result> Handle(DeleteProductCommand request, CancellationToken cancellationToken)
    {
        var product = await _productRepository.GetByIdAsync(request.Id, cancellationToken);
        if (product == null || product.IsDeleted)
            return Result.Failure("Product not found.");

        product.MarkDeleted();
        await _productRepository.UpdateAsync(product, cancellationToken);

        await _cacheService.ClearProductsCacheAsync();

        return Result.Ok();
    }
}
