from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import JSONResponse
from entities.chat_history import ChatHistory
from services.chat_service import send_message


router = APIRouter()
chatHistory = ChatHistory()


@router.post("/chat")
async def chat_test(request: Request):
    data = await request.json()

    if not data:
        raise HTTPException(
            status_code=500, detail=f"Request not found"
        )

    message = data.get("message")
    print(message)

    if not message:
        raise HTTPException(
            status_code=400, detail=f"Empty Request Body"
        )

    response = await send_message(message)

    if not response:
        raise HTTPException(
            status_code=500, detail=f"Error to process the message"
        )

    return JSONResponse(content=response, status_code=status.HTTP_200_OK)
