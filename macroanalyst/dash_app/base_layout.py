# Describes base Dash layout

html_layout = '''<!DOCTYPE html>
                    <html>
                        <head>
                            {%metas%}
                            <title>MA Dash</title>
                            <link rel="icon" href="{{ url_for('static', filename='img/favicon/favicon.ico') }}">
                            {%css%}
                        </head>
                        <body>
                            {%app_entry%}
                            <footer>
                                {%config%}
                                {%scripts%}
                                {%renderer%}
                                <footer class="bg-light py-5">
                                    <div class="container"">
                                        <p class="text-center text-muted mb-0">Made with <i class="fas fa-heart text-danger mb-4"></i> in four time zones.</p>
                                        <div class="small text-center text-muted">Copyright &copy; 2019 - <a href="#">Licensing information</a>
                                        </div>
                                    </div>
                                </footer>
                            </footer>
                        </body>
                    </html>'''