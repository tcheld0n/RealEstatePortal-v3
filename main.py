from app.controllers.user_controller import UserController
from app.controllers.property_controller import PropertyController
from app.controllers.mortgage_controller import MortgageController
from app.controllers.visit_controller import VisitController
from app.controllers.market_analysis_controller import MarketAnalysisController
from app.controllers.review_controller import ReviewController
from app.data.database import db

def menu():
    user_controller = UserController()
    property_controller = PropertyController()
    mortgage_controller = MortgageController()
    visit_controller = VisitController(property_controller, user_controller)
    market_analysis_controller = MarketAnalysisController(property_controller)
    review_controller = ReviewController()
    logged_user = None

    while True:
        try:
            print("\n===== Portal de Imóveis =====")
            print("1 - Cadastrar Usuário")
            print("2 - Login")
            print("3 - Cadastrar Propriedade")
            print("4 - Buscar Propriedades")
            print("5 - Calcular Financiamento")
            print("6 - Agendar visita")
            print("7 - Avaliar Propriedade")
            print("8 - Exibir Avaliações")
            print("9 - Análise de Mercado")
            print("10 - Logout")
            print("0 - Sair")

            option = input("Escolha uma opção: ")

            if option == "1":
                name = input("Digite o nome do usuário: ")
                email = input("Digite o email do usuário: ")
                password = input("Digite a senha: ")
                user_type = input("Digite o tipo de usuário (Cliente ou Agente): ")
                user_controller.register_user(name, email, password, user_type)

            elif option == "2":
                logged_user = user_controller.login()


            elif option == "3":
                if logged_user is None:
                    print("Erro: Nenhum usuário logado.")
                elif logged_user.get_role() != "Agente":
                    print("Erro: Apenas agentes podem cadastrar uma propriedade.")
                else:
                    title = input("Digite o título da propriedade: ")
                    description = input("Digite a descrição da propriedade: ")
                    price = float(input("Digite o preço da propriedade: "))
                    location = input("Digite a localização da propriedade: ")
                    property_category = input("Digite o tipo do imóvel (Casa/Apartamento/Terreno): ")
                    while property_category not in {"Casa", "Apartamento", "Terreno"}:
                        print("Erro: Categoria inválida. Use: Casa, Apartamento ou Terreno.")
                        property_category = input("Digite o tipo do imóvel (Casa/Apartamento/Terreno): ")
                    transaction_type = input("Digite o tipo de transação (Venda/Aluguel): ")
                    while transaction_type not in {"Venda", "Aluguel"}:
                        print("Erro: Transação inválida. Use: Venda ou Aluguel.")
                        transaction_type = input("Digite o tipo de transação (Venda/Aluguel): ")
                    new_property = property_controller.add_property(
                        id=None,
                        title=title,
                        description=description,
                        price=price,
                        location=location,
                        property_category=property_category,
                        transaction_type=transaction_type,
                        agent=logged_user
                    )
                    print(f"Propriedade '{new_property.title}' cadastrada com sucesso!")

            elif option == "4":
                print("\n===== Buscar Propriedades =====")
                search_by = input("Buscar por: 0 - Todas | 1 - Localização | 2 - Tipo | 3 - Faixa de preço: ")
                if search_by == "0":
                    results = property_controller.search_all_properties()
                elif search_by == "1":
                    location = input("Digite a localização: ")
                    results = property_controller.search_property_by_location(location)
                elif search_by == "2":
                    property_category = input("Digite o tipo do imóvel (Casa/Apartamento/Terreno): ")
                    results = property_controller.search_property_by_type(property_category)
                elif search_by == "3":
                    min_price = float(input("Digite o preço mínimo: "))
                    max_price = float(input("Digite o preço máximo: "))
                    results = property_controller.search_property_by_price_range(min_price, max_price)
                else:
                    print("Opção inválida.")
                    return
                if results:
                    print("\nResultados da busca:")
                    for prop in results:
                        print(prop)
                else:
                    print("Nenhuma propriedade encontrada.")

            elif option == "5":
                # Calcular Financiamento
                print("\n===== Calcular Financiamento =====")
                price = float(input("Digite o preço do imóvel: "))
                interest_rate = float(input("Digite a taxa de juros anual (em %): "))
                years = int(input("Digite o período de pagamento (em anos): "))

                # Calcula o financiamento diretamente
                mortgage = mortgage_controller.calculate_mortgage(price, interest_rate, years)

                # Exibe o resultado com base no atributo monthly_payment
                print(f"\nO valor da parcela mensal será: R$ {mortgage.monthly_payment:.2f}")

            elif option == "6":
                print("\n===== Agendar Visita =====")
                if logged_user is None:
                    print("Erro: Nenhum usuário logado.")
                else:
                    property_id = int(input("Digite o ID da propriedade para agendar visita: "))
                    date_time = input("Digite a data e hora para a visita (ex: 2025-03-14 10:00): ")

                    # Agendar visita
                    new_visit = visit_controller.schedule_visit(
                        id=len(db.get_visits()) + 1,
                        client_id=logged_user.id,
                        agent_id=logged_user.id,  # O agente pode ser o próprio usuário logado ou outro
                        property_id=property_id,
                        date_time=date_time
                    )
                    if new_visit:
                        print("Visita agendada com sucesso!")
                    else:
                        print("Erro ao agendar a visita. Verifique a disponibilidade.")

            elif option == "7":
                print("\n===== Avaliar Propriedade =====")
                if logged_user is None:
                    print("Erro: Nenhum usuário logado.")
                else:
                    property_id = int(input("Digite o ID da propriedade para avaliar: "))
                    rating = int(input("Digite a nota de avaliação (1-5): "))
                    comment = input("Digite um comentário (opcional): ")
                    # Adicionar avaliação usando o ReviewController
                    new_review = review_controller.add_review(
                        id=len(db.get_reviews()) + 1,
                        reviewer_id=logged_user.id,
                        property_id=property_id,
                        rating=rating,
                        comment=comment
                    )
                    if new_review:
                        print("Avaliação adicionada com sucesso!")
                    else:
                        print("Erro ao adicionar a avaliação.")

            elif option == "8":
                print("\n===== Exibir Avaliações =====")
                property_id = int(input("Digite o ID da propriedade para exibir avaliações: "))

                # Obter avaliações usando o ReviewController
                reviews = review_controller.get_reviews_by_property()
                if reviews:
                    print("Avaliações:")
                    for review in reviews:
                        print(
                            f"Cliente {review['reviewer_id']} - Nota: {review['rating']} - Comentário: {review['comment']}")
                else:
                    print("Nenhuma avaliação encontrada.")

            elif option == "9":
                print("\n===== Análise de Mercado =====")
                location = input("Digite a localização para análise de mercado: ")
                analysis = market_analysis_controller.get_market_analysis(location)

                if analysis:
                    print(f"\nPreço Médio: R$ {analysis['avg_price']:.2f}")
                    print(f"Número de Imóveis para Venda: {analysis['num_sale']}")
                    print(f"Número de Imóveis para Aluguel: {analysis['num_rent']}")
                else:
                    print("Nenhuma análise disponível para esta localização.")

            elif option == "10":
                if logged_user:
                    print(f"Logout realizado. Até mais, {logged_user.name}!")
                    logged_user = None
                else:
                    print("Nenhum usuário logado.")

            elif option == "0":
                print("Saindo do sistema...")
                break

            else:
                print("Opção inválida.")

        except Exception as e:
            print(f"\nErro inesperado: {e}")
            print("Voltando ao menu principal...")

if __name__ == "__main__":
    menu()