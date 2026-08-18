namespace PetShop.Catalog.Api.Controllers;

using MediatR;
using Microsoft.AspNetCore.Mvc;
using PetShop.Catalog.Application.Commands;
using PetShop.Catalog.Application.DTOs;
using PetShop.Catalog.Application.Queries;
using PetShop.Catalog.Application.Validators;
using FluentValidation;

[ApiController]
[Route("api/catalog/products")]
[Produces("application/json")]
public class ProductsController : ControllerBase
{
    private readonly IMediator _mediator;
    private readonly IValidator<CreateProductCommand> _createValidator;
    private readonly IValidator<UpdateProductCommand> _updateValidator;

    public ProductsController(
        IMediator mediator,
        IValidator<CreateProductCommand> createValidator,
        IValidator<UpdateProductCommand> updateValidator)
    {
        _mediator = mediator;
        _createValidator = createValidator;
        _updateValidator = updateValidator;
    }

    /// <summary>
    /// Browse/search products with pagination and filtering.
    /// </summary>
    [HttpGet]
    [ProducesResponseType(typeof(Paging<ProductResponse>), StatusCodes.Status200OK)]
    public async Task<IActionResult> GetProducts(
        [FromQuery] string? search,
        [FromQuery] Guid? categoryId,
        [FromQuery] decimal? minPrice,
        [FromQuery] decimal? maxPrice,
        [FromQuery] int page = 1,
        [FromQuery] int pageSize = 20)
    {
        var query = new GetProductsQuery(search, categoryId, minPrice, maxPrice, page, pageSize);
        var result = await _mediator.Send(query);

        if (!result.IsSuccess)
            return NotFound(result.Error);

        return Ok(result.Value);
    }

    /// <summary>
    /// Get a single product by ID.
    /// </summary>
    [HttpGet("{id:guid}")]
    [ProducesResponseType(typeof(ProductResponse), StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public async Task<IActionResult> GetProductById(Guid id)
    {
        var query = new GetProductByIdQuery(id);
        var result = await _mediator.Send(query);

        if (!result.IsSuccess)
            return NotFound(result.Error);

        return Ok(result.Value);
    }

    /// <summary>
    /// Create a new product (admin only).
    /// </summary>
    [HttpPost]
    [Authorize(Roles = "Admin")]
    [ProducesResponseType(typeof(ProductResponse), StatusCodes.Status201Created)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> CreateProduct([FromBody] CreateProductRequest request)
    {
        var command = new CreateProductCommand(
            request.Name, request.Description, request.Price,
            request.CategoryId, request.ImageUrl, request.InventoryCount);

        var errors = await _createValidator.ValidateAndThrowAsync(command);
        var result = await _mediator.Send(command);

        if (!result.IsSuccess)
            return BadRequest(result.Error);

        return CreatedAtAction(nameof(GetProductById), new { id = result.Value.Id }, result.Value);
    }

    /// <summary>
    /// Update an existing product (admin only).
    /// </summary>
    [HttpPut("{id:guid}")]
    [Authorize(Roles = "Admin")]
    [ProducesResponseType(typeof(ProductResponse), StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public async Task<IActionResult> UpdateProduct(Guid id, [FromBody] UpdateProductRequest request)
    {
        var command = new UpdateProductCommand(id, request.Name, request.Description, request.Price, request.CategoryId, request.ImageUrl);

        var errors = await _updateValidator.ValidateAndThrowAsync(command);
        var result = await _mediator.Send(command);

        if (!result.IsSuccess)
            return NotFound(result.Error);

        return Ok(result.Value);
    }

    /// <summary>
    /// Delete a product (admin only, soft delete).
    /// </summary>
    [HttpDelete("{id:guid}")]
    [Authorize(Roles = "Admin")]
    [ProducesResponseType(StatusCodes.Status204NoContent)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public async Task<IActionResult> DeleteProduct(Guid id)
    {
        var command = new DeleteProductCommand(id);
        var result = await _mediator.Send(command);

        if (!result.IsSuccess)
            return NotFound(result.Error);

        return NoContent();
    }
}
