
# Describes base Dash layout

html_layout = '''<!DOCTYPE html>
                    <html>
                        <head>
                            {%metas%}
                            <title>Daash App</title>
                            <link rel="shortcut icon" href="{{ url_for('static', filename='img/favicon/favicon.ico') }}">
                            {%css%}
                        </head>
                        <body>
                            {%app_entry%}
                            <footer>
                                {%config%}
                                {%scripts%}
                                {%renderer%}
                            </footer>
                        </body>
                    </html>'''