using FluentValidation;
using PetShop.Catalog.Application.Commands;

namespace PetShop.Catalog.Application.Validators;

public class CreateProductValidator : AbstractValidator<CreateProductCommand>
{
    public CreateProductValidator()
    {
        RuleFor(x => x.Name).NotEmpty().MaximumLength(200);
        RuleFor(x => x.Description).MaximumLength(5000);
        RuleFor(x => x.Price).GreaterThan(0);
        RuleFor(x => x.CategoryId).NotEqual(Guid.Empty);
        RuleFor(x => x.InventoryCount).GreaterThanOrEqualTo(0);
    }
}

public class UpdateProductValidator : AbstractValidator<UpdateProductCommand>
{
    public UpdateProductValidator()
    {
        RuleFor(x => x.Id).NotEqual(Guid.Empty);
        RuleFor(x => x.Name).MaximumLength(200).MustBeNullableOrNotEmpty();
        RuleFor(x => x.Description).MaximumLength(5000).MustBeNullableOrNotEmpty();
        RuleFor(x => x.Price).GreaterThan(0).When(x => x.Price.HasValue);
    }
}

public static class ValidatorExtensions
{
    public static IRuleBuilder<T, string?> MustBeNullableOrNotEmpty<T>(
        this IRuleBuilder<T, string?> ruleBuilder)
    {
        return ruleBuilder.Must(name => string.IsNullOrWhiteSpace(name) || !string.IsNullOrEmpty(name.Trim()));
    }
}
