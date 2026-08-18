FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /source

COPY Directory.Build.props ./
COPY src/PetShop.Api/PetShop.Api.csproj src/PetShop.Api/
COPY src/PetShop.Shared/src/PetShop.Shared.Domain/PetShop.Shared.Domain.csproj src/PetShop.Shared/src/PetShop.Shared.Domain/
COPY src/PetShop.Shared/src/PetShop.Shared.Application/PetShop.Shared.Application.csproj src/PetShop.Shared/src/PetShop.Shared.Application/
COPY src/PetShop.Shared/src/PetShop.Shared.Infrastructure/PetShop.Shared.Infrastructure.csproj src/PetShop.Shared/src/PetShop.Shared.Infrastructure/
COPY src/PetShop.Catalog/src/PetShop.Catalog.Domain/PetShop.Catalog.Domain.csproj src/PetShop.Catalog/src/PetShop.Catalog.Domain/
COPY src/PetShop.Catalog/src/PetShop.Catalog.Application/PetShop.Catalog.Application.csproj src/PetShop.Catalog/src/PetShop.Catalog.Application/
COPY src/PetShop.Catalog/src/PetShop.Catalog.Infrastructure/PetShop.Catalog.Infrastructure.csproj src/PetShop.Catalog/src/PetShop.Catalog.Infrastructure/
COPY src/PetShop.Catalog/PetShop.Catalog.csproj src/PetShop.Catalog/
COPY src/PetShop.Orders/src/PetShop.Orders.Domain/PetShop.Orders.Domain.csproj src/PetShop.Orders/src/PetShop.Orders.Domain/
COPY src/PetShop.Orders/src/PetShop.Orders.Application/PetShop.Orders.Application.csproj src/PetShop.Orders/src/PetShop.Orders.Application/
COPY src/PetShop.Orders/src/PetShop.Orders.Infrastructure/PetShop.Orders.Infrastructure.csproj src/PetShop.Orders/src/PetShop.Orders.Infrastructure/
COPY src/PetShop.Orders/PetShop.Orders.csproj src/PetShop.Orders/
COPY src/PetShop.Users/src/PetShop.Users.Domain/PetShop.Users.Domain.csproj src/PetShop.Users/src/PetShop.Users.Domain/
COPY src/PetShop.Users/src/PetShop.Users.Application/PetShop.Users.Application.csproj src/PetShop.Users/src/PetShop.Users.Application/
COPY src/PetShop.Users/src/PetShop.Users.Infrastructure/PetShop.Users.Infrastructure.csproj src/PetShop.Users/src/PetShop.Users.Infrastructure/
COPY src/PetShop.Users/PetShop.Users.csproj src/PetShop.Users/
COPY src/PetShop.Auth/src/PetShop.Auth.Domain/PetShop.Auth.Domain.csproj src/PetShop.Auth/src/PetShop.Auth.Domain/
COPY src/PetShop.Auth/src/PetShop.Auth.Application/PetShop.Auth.Application.csproj src/PetShop.Auth/src/PetShop.Auth.Application/
COPY src/PetShop.Auth/src/PetShop.Auth.Infrastructure/PetShop.Auth.Infrastructure.csproj src/PetShop.Auth/src/PetShop.Auth.Infrastructure/
COPY src/PetShop.Auth/PetShop.Auth.csproj src/PetShop.Auth/

RUN dotnet restore src/PetShop.Api/PetShop.Api.csproj

COPY . .
RUN dotnet publish src/PetShop.Api/PetShop.Api.csproj \
    --configuration Release \
    --no-restore \
    --output /app/publish \
    /p:UseAppHost=false

FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS final
WORKDIR /app
EXPOSE 8080
ENV ASPNETCORE_HTTP_PORTS=8080
COPY --from=build /app/publish .
ENTRYPOINT ["dotnet", "PetShop.Api.dll"]
