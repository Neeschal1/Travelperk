from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>TravelPerk</title>
        <!-- Google Fonts: Poppins -->
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">

        <style>
            body {
                font-family: 'Poppins', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f9f9f9;
            }

            .container {
                min-height: 80vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: center;
                padding: 20px;
            }

            h1 {
                font-size: 3rem;
                margin-bottom: 10px;
                letter-spacing: 1px;
            }

            h1 span {
                color: #025FC9;
            }

            p {
                max-width: 650px;
                font-size: 1rem;
                opacity: 0.9;
                margin-bottom: 30px;
            }
            
            footer {
                position: absolute;
                bottom: 15px;
                font-size: 0.9rem;
                opacity: 0.7;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Travel<span>Perk</span></h1>
            <p>
                TravelPerk is a full-stack travel and booking web application designed to simplify trip planning and booking for users. The platform provides travel packages, flight booking, hotel reservations, car rentals, local guides, and cuisine recommendations — all supported by an AI-powered chatbot guide. The system is built using modern UI/UX principles, a scalable backend, a responsive frontend, and an AI RAG-based chatbot to assist users at every step.
            </p>

            <footer>
                © 2025 TravelPerk · Smart Travel Made Simple
            </footer>
        </div>
    </body>
    </html>
    """)
