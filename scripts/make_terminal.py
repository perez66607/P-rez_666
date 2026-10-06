def create_terminal():
    art_grid = [
        "         BB                               BB         ",
        "        BB                                 BB        ",
        "       BB                                   BB       ",
        "       BB      WWWW     WWWW     WWWW       BB       ",
        "       BB     WW       WW       WW          BB       ",
        "       BB     WW       WW       WW          BB       ",
        "       BB     WWWWW    WWWWW    WWWWW       BB       ",
        "       BB     WW  WW   WW  WW   WW  WW      BB       ",
        "       BB     WW  WW   WW  WW   WW  WW      BB       ",
        "       BB      WWWWW    WWWWW    WWWWW      BB       ",
        "       BB                                   BB       ",
        "        BB                                 BB        ",
        "         BB                               BB         "
    ]
    
    pixel_size = 5
    start_x = 35
    start_y = 85
    pixels_svg = ""
    
    for row_idx, row in enumerate(art_grid):
        for col_idx, char in enumerate(row):
            x = start_x + (col_idx * pixel_size)
            y = start_y + (row_idx * pixel_size)
            if char == 'B':
                pixels_svg += f'<rect x="{x}" y="{y}" width="{pixel_size+.5}" height="{pixel_size+.5}" fill="#00a8ff" rx="1"/>\n'
            elif char == 'W':
                pixels_svg += f'<rect x="{x}" y="{y}" width="{pixel_size+.5}" height="{pixel_size+.5}" fill="#ff7b72" rx="1"/>\n'

    svg = f"""<svg width="860" height="340" viewBox="0 0 860 340" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#0d1117"/>
            <stop offset="100%" stop-color="#161b22"/>
        </linearGradient>
        <style>
            .window {{ fill: url(#bg); stroke: #30363d; stroke-width: 1px; rx: 8px; }}
            .topbar {{ fill: #010409; }}
            .dot-red {{ fill: #ff5f56; }}
            .dot-yellow {{ fill: #ffbd2e; }}
            .dot-green {{ fill: #27c93f; }}
            
            .text {{ font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace; font-size: 14px; fill: #c9d1d9; }}
            .key {{ fill: #79c0ff; font-weight: bold; }}
            .val {{ fill: #8b949e; }}
            
            .typing-container {{
                overflow: hidden;
                white-space: nowrap;
                border-right: 2px solid #c9d1d9;
                width: 0;
                animation: typing 1.2s steps(30, end) forwards, blink 0.8s step-end infinite;
            }}
            .fade {{ opacity: 0; animation: fadeIn 0.4s ease-in forwards; }}
            .f-1 {{ animation-delay: 1.1s; }}
            .f-2 {{ animation-delay: 1.3s; }}
            .f-3 {{ animation-delay: 1.5s; }}
            .f-4 {{ animation-delay: 1.7s; }}
            .f-5 {{ animation-delay: 1.9s; }}
            .f-6 {{ animation-delay: 2.1s; }}
            .f-7 {{ animation-delay: 2.3s; }}
            .f-8 {{ animation-delay: 2.5s; }}
            
            @keyframes typing {{
                from {{ width: 0; }}
                to {{ width: 300px; }}
            }}
            @keyframes blink {{
                from, to {{ border-color: transparent; }}
                50% {{ border-color: #c9d1d9; }}
            }}
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(4px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
            
            .progress-bg {{ fill: #21262d; rx: 3px; }}
            .progress-bar {{ rx: 3px; }}
        </style>
    </defs>

    <rect width="100%" height="100%" class="window" />
    <path d="M 0 8 Q 0 0 8 0 L 852 0 Q 860 0 860 8 L 860 30 L 0 30 Z" class="topbar" />
    <circle cx="20" cy="15" r="6" class="dot-red" />
    <circle cx="40" cy="15" r="6" class="dot-yellow" />
    <circle cx="60" cy="15" r="6" class="dot-green" />
    <text x="430" y="20" font-family="sans-serif" font-size="12px" fill="#8b949e" text-anchor="middle">perez66607@github: ~ (zsh)</text>

    <!-- Logo 666 Pixel Art -->
    <g class="fade" style="animation-delay: 0.3s;">
        {pixels_svg}
    </g>

    <!-- Bloque de texto con líneas totalmente separadas y seguras -->
    <g class="text" transform="translate(295, 65)">
        <foreignObject x="0" y="0" width="450" height="25">
            <div xmlns="http://www.w3.org/1999/xhtml" class="text typing-container" style="color: #c9d1d9; font-size: 14px;">
                <span style="color: #3fb950; font-weight: bold;">perez66607@github</span>:<span style="color: #58a6ff; font-weight: bold;">~</span>$ <span style="color: #f0f6fc; font-weight: bold;">./web_dev.sh</span>
            </div>
        </foreignObject>
        
        <text x="0" y="45" class="fade f-1"><tspan class="key">Role</tspan>       <tspan class="val">~ Web Developer &amp; UI Designer</tspan></text>
        <text x="0" y="75" class="fade f-2"><tspan class="key">Location</tspan>   <tspan class="val">~ El Ejido, Andalusia</tspan></text>
        <text x="0" y="105" class="fade f-3"><tspan class="key">Focus</tspan>      <tspan class="val">~ Interactive Web Apps &amp; Clicker Games</tspan></text>
        <text x="0" y="135" class="fade f-4"><tspan class="key">Tools</tspan>      <tspan class="val">~ HTML, CSS, JavaScript, VS Code</tspan></text>
        
        <text x="0" y="175" class="fade f-5" fill="#58a6ff" font-weight="bold">Tech Stack &amp; Skills</text>
        
        <!-- Barras de progreso separadas y abajo del todo -->
        <text x="0" y="205" class="fade f-6" font-size="12px" fill="#c9d1d9">HTML / CSS / UI</text>
        <rect x="120" y="195" width="160" height="9" class="progress-bg fade f-6" />
        <rect x="120" y="195" width="145" height="9" class="progress-bar fade f-6" fill="#00a8ff" />
        
        <text x="0" y="230" class="fade f-7" font-size="12px" fill="#c9d1d9">JavaScript / Web</text>
        <rect x="120" y="220" width="160" height="9" class="progress-bg fade f-7" />
        <rect x="120" y="220" width="130" height="9" class="progress-bar fade f-7" fill="#ffa657" />
        
        <text x="0" y="255" class="fade f-8" font-size="12px" fill="#c9d1d9">Python / Scripts</text>
        <rect x="120" y="245" width="160" height="9" class="progress-bg fade f-8" />
        <rect x="120" y="245" width="115" height="9" class="progress-bar fade f-8" fill="#3fb950" />
    </g>
    </svg>"""

    with open("terminal.svg", "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    create_terminal()
