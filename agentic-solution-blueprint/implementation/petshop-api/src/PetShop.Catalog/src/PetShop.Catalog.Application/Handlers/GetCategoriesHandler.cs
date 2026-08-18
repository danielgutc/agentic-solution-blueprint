namespace PetShop.Catalog.Application.Handlers;

using MediatR;
using PetShop.Catalog.Application.DTOs;
using PetShop.Catalog.Application.Queries;
using PetShop.Catalog.Infrastructure.Repositories;

public class GetCategoriesHandler : IRequestHandler<GetCategoriesQuery, Result<IEnumerable<CategoryResponse>>>
{
    private readonly ICategoryRepository _categoryRepository;

    public GetCategoriesHandler(ICategoryRepository categoryRepository)
    {
        _categoryRepository = categoryRepository;
    }

    public async Task<Result<IEnumerable<CategoryResponse>>> Handle(GetCategoriesQuery request, CancellationToken cancellationToken)
    {
        var categories = await _categoryRepository.GetAllAsync(cancellationToken);
        return Result<IEnumerable<CategoryResponse>>.Success(
            categories.Where(c => !c.IsDeleted).Select(MapToResponse)
        );
    }

    private static CategoryResponse MapToResponse(PetShop.Catalog.Domain.Entities.Category category)
    {
        return new CategoryResponse(category.Id, category.Name, category.Description, category.ParentCategoryId);
    }
}
