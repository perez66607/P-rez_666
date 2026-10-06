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
        "       BB                                   BB       ",
        "        BB                                 BB        ",
        "         BB                               BB         "
    ]
    
    pixel_size = 5
    start_x = 35
    start_y = 55
    pixels_svg = ""
    
    for row_idx, row in enumerate(art_grid):
        for col_idx, char in enumerate(row):
            x = start_x + (col_idx * pixel_size)
            y = start_y + (row_idx * pixel_size)
            if char == 'B':
                pixels_svg += f'<rect x="{x}" y="{y}" width="{pixel_size+.5}" height="{pixel_size+.5}" fill="#00a8ff" rx="1"/>\n'
            elif char == 'W':
                pixels_svg += f'<rect x="{x}" y="{y}" width="{pixel_size+.5}" height="{pixel_size+.5}" fill="#ff7b72" rx="1"/>\n'

    svg = f"""<svg width="860" height="320" viewBox="0 0 860 320" xmlns="http://www.w3.org/2000/svg">
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
            
            .text {{ font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace; font-size: 13.5px; fill: #c9d1d9; }}
            .key {{ fill: #79c0ff; font-weight: bold; }}
            .val {{ fill: #8b949e; }}
            
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
    <g>
        {pixels_svg}
    </g>

    <!-- Bloque de texto y barras limpio y estático sin solapamientos -->
    <g class="text" transform="translate(290, 45)">
        <text x="0" y="20"><tspan style="color: #3fb950; font-weight: bold;">perez66607@github</tspan>:<tspan style="color: #58a6ff; font-weight: bold;">~</tspan>$ <tspan style="color: #f0f6fc; font-weight: bold;">./web_dev.sh</tspan></text>
        
        <text x="0" y="50"><tspan class="key">Role</tspan>       <tspan class="val">~ Web Developer &amp; UI Designer</tspan></text>
        <text x="0" y="75"><tspan class="key">Location</tspan>   <tspan class="val">~ El Ejido, Andalusia</tspan></text>
        <text x="0" y="100"><tspan class="key">Focus</tspan>      <tspan class="val">~ Interactive Web Apps &amp; Clicker Games</tspan></text>
        <text x="0" y="125"><tspan class="key">Tools</tspan>      <tspan class="val">~ HTML, CSS, JavaScript, VS Code</tspan></text>
        
        <text x="0" y="160" fill="#58a6ff" font-weight="bold">Tech Stack &amp; Skills</text>
        
        <text x="0" y="185" font-size="12px" fill="#c9d1d9">HTML / CSS / UI</text>
        <rect x="120" y="176" width="160" height="8" class="progress-bg" />
        <rect x="120" y="176" width="145" height="8" class="progress-bar" fill="#00a8ff" />
        
        <text x="0" y="210" font-size="12px" fill="#c9d1d9">JavaScript / Web</text>
        <rect x="120" y="201" width="160" height="8" class="progress-bg" />
        <rect x="120" y="201" width="130" height="8" class="progress-bar" fill="#ffa657" />
        
        <text x="0" y="235" font-size="12px" fill="#c9d1d9">Python / Scripts</text>
        <rect x="120" y="226" width="160" height="8" class="progress-bg" />
        <rect x="120" y="226" width="115" height="8" class="progress-bar" fill="#3fb950" />
    </g>
    </svg>"""

    with open("terminal-v2.svg", "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    create_terminal()
