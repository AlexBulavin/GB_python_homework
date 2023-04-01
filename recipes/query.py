__author__ = 'Alex Bulavin'

url = 'https://content.dev.skydom.company/v1/graphql'
headers = {'Content-type': 'application/json'}

path_to_cert = '/Users/alex/Documents/Python_projects/tubeles/venv/lib/python3.9/site-packages/future/backports/test/ssl_cert.pem'

graphql_query = """
query getRecipes($deviceIds: [Int!], $categoryId: Int, $descriptionIds: [Int!], $locale: String!, $recipeId: Int, $query: String, $offset: Int, $limit: Int) {
  recipe_description(
    distinct_on: [recipe_id]
    where: {
      devices: {device_id: {_in: $deviceIds}},
      id: {_in: $descriptionIds},
      recipe: {
        id: {_eq: $recipeId}
        recipe_tags: {tag_id: {_eq: $categoryId}}
        translatable_fields: {
          name: {_ilike: $query},
        }
      },
      translatable_fields: {
        locale: {_eq: $locale}
      }
    },
    limit: $limit,
    offset: $offset
  ) {
    id
    state
    energy
    cooktime
    translatable_fields(where: {locale: {_eq: $locale}}) {
      description
    }
    recipe {
      id
      state
      image_id
      translatable_fields(where: {locale: {_eq: $locale}}) {
        name
      }
    }
    recipe_ingredients {
            id
            state
            quantity
            quantity_unit {
                id
                type
                multiplier
                translatable_fields(where: {locale: {_eq: $locale}}) {
                    name
                }
            }
            ingredient {
                id
                state
                translatable_fields(where: {locale: {_eq: $locale}}) {
                    name
                }
            }
        }
    recipe_steps {
      id
      time
      temperature
      program
      tools {
        id
        time
        tool {
          id
          translatable_fields(where: {locale: {_eq: $locale}}) {
            name
          }
          image_id
        }
      }
    }
  }
}
"""

variables = {
    "deviceIds": 0,
    "categoryId": None,
    "descriptionIds": None,
    "locale": "ru",
    "recipeId": None,
    "query": None,
    "offset": 0,
    "limit": None
}

device_query = """
query MyQuery {
  SearchModels($search: String!, $limit: Int, $locale: String!, $offset: Int, $path: [String!], $state: available) {
    broadcast_name
    catalog
    catalog_image_id
    category_id
    commit_id
    id
    image_id
    kind
    name
    pairing_image_id
    pairing_text
    parent_id
    protocols
    slug
    state
    transport
    vendor {
      id
      name
    }
  }
}"""
search = input("Введите поисковой запрос, например: RMC-M800S ")
device_var = {
    "search": search,
    "limit": 10,
    "locale": "ru",
    "offset": 0,  # Сдвиг в запросе данных относительно нулевого значения. Используется при пагинации
    "path": ["Devices"],
    "state": "available"
}
