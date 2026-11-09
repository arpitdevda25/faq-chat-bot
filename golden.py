
GOLDEN = [

    # Remote-related questions
    {
        "q": "My fan remote stopped working. What should I do?",
        "must": ["batteries"],
        "source": "kb-01"
    },

    {
        "q": "Do I need to replace remote batteries?",
        "must": ["batteries"],
        "source": "kb-01"
    },

    {
        "q": "Where should I stand to use the remote?",
        "must": ["5 metres"],
        "source": "kb-01"
    },

    # Wi-Fi-related questions
    {
        "q": "Does the fan work with 5 GHz Wi-Fi?",
        "must": ["2.4 ghz"],
        "source": "kb-02"
    },

    {
        "q": "Does the fan support 2.4 GHz Wi-Fi?",
        "must": ["2.4 ghz"],
        "source": "kb-02"
    },

    {
        "q": "Which Wi-Fi band does the fan support?",
        "must": ["2.4 ghz"],
        "source": "kb-02"
    },

    # Warranty-related questions
    {
        "q": "Is the motor warranty valid without the invoice?",
        "must": ["invoice"],
        "source": "kb-03"
    },

    {
        "q": "Do I need a purchase invoice for warranty?",
        "must": ["invoice"],
        "source": "kb-03"
    },

    {
        "q": "What document is required for motor warranty?",
        "must": ["invoice"],
        "source": "kb-03"
    },

    # Questions outside the chatbot's knowledge
    {
        "q": "What is the price of gold today?",
        "must": ["don't know"],
        "source": None
    },

    {
        "q": "What will the weather be tomorrow?",
        "must": ["don't know"],
        "source": None
    },

    {
        "q": "Who is the CEO of this company?",
        "must": ["don't know"],
        "source": None
    }
]
