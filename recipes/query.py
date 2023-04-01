__author__ = 'Alex Bulavin'

# from json_to_csv import device_ids

query = """
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
    "deviceIds": None, #device_ids,
    "categoryId": None,
    "descriptionIds": None,
    "locale": "ru_RU",
    "recipeId": None,
    "query": None,
    "offset": 0,
    "limit": 100
}

url = 'https://cmsql.skydom.company/v1/graphql'
headers = {'Content-type': 'application/json'}

path_to_cert = '/Users/alex/Documents/Python_projects/tubeles/venv/lib/python3.9/site-packages/future/backports/test/ssl_cert.pem'