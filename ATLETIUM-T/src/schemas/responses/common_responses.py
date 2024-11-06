from starlette.responses import JSONResponse

ItemCreatedSuccessfully: JSONResponse = JSONResponse(
        status_code=201,
        content={"message": "Item created successfully"}
    )

ItemUpdatedSuccessfully: JSONResponse = JSONResponse(
    status_code=200,
    content={"message": "Item updated successfully"}
)
