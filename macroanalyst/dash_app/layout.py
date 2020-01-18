html_layout = '''<!DOCTYPE html>
                    <html>
                        <head>
                            {%metas%}
                            <title>{%title%}</title>
                            {%favicon%}
                            {%css%}
                        </head>
                        <body>
                            <nav>
                              <a href="/"><i class="fas fa-home"></i> Home</a>
                              <a href="/dashapp/"><i class="fas fa-chart-line"></i> Embdedded Plotly Dash</a>
                            </nav>
                            {%app_entry%}
                            <footer>
                                {%config%}
                                {%scripts%}
                                {%renderer%}
                            </footer>
                        </body>
                    </html>'''