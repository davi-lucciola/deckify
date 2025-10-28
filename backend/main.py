from fastapi import FastAPI


app = FastAPI(
    title='Deckify API', 
    description='API for manage deckify users, decks and cards'
)


@app.get('/health', summary='Health Check', tags=['Infra'])
def health_check():
    return {'status': 'ok'}
