class SchemaAssertions:
    @staticmethod
    def validate_schema(schema_model, json_data):
        schema_model(**json_data)