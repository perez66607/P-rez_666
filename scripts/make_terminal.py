def create_terminal():
    svg = """<svg width="860" height="280" viewBox="0 0 860 280" xmlns="http://www.w3.org/2000/svg">
    <style>
        .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1px; rx: 8px; }
        .topbar { fill: #161b22; }
        .dot-red { fill: #ff5f56; }
        .dot-yellow { fill: #ffbd2e; }
        .dot-green { fill: #27c93f; }
        .text { font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace; font-size: 14px; fill: #c9d1d9; }
        .prompt { fill: #3fb950; font-weight: bold; }
        .dir { fill: #58a6ff; font-weight: bold; }
        .cmd { fill: #f0f6fc; }
        .key { fill: #79c0ff; font-weight: bold; }
        .val { fill: #8b949e; }
        .ascii { font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace; font-size: 14px; fill: #58a6ff; white-space: pre; font-weight: bold; }
    </style>
    
    <rect width="100%" height="100%" class="bg" />
    <path d="M 0 8 Q 0 0 8 0 L 852 0 Q 860 0 860 8 L 860 30 L 0 30 Z" class="topbar" />
    <circle cx="20" cy="15" r="6" class="dot-red" />
    <circle cx="40" cy="15" r="6" class="dot-yellow" />
    <circle cx="60" cy="15" r="6" class="dot-green" />
    <text x="430" y="20" font-family="sans-serif" font-size="12px" fill="#8b949e" text-anchor="middle">perez66607@github: ~</text>

    <!-- ASCII Segura -->
    <text x="40" y="60" class="ascii">
        <tspan x="40" dy="0">   .-----------------.   </tspan>
        <tspan x="40" dy="18">  | .---------------. |  </tspan>
        <tspan x="40" dy="18">  | |   _______     | |  </tspan>
        <tspan x="40" dy="18">  | |  |  ___  |    | |  </tspan>
        <tspan x="40" dy="18">  | |  | |___| |    | |  </tspan>
        <tspan x="40" dy="18">  | |  |  _____|    | |  </tspan>
        <tspan x="40" dy="18">  | |  | |          | |  </tspan>
        <tspan x="40" dy="18">  | |  |_|          | |  </tspan>
        <tspan x="40" dy="18">  | '---------------' |  </tspan>
        <tspan x="40" dy="18">   '-----------------'   </tspan>
    </text>

    <!-- Datos Neofetch -->
    <text x="280" y="70" class="text">
        <tspan x="280" dy="0"><tspan class="prompt">perez66607@github</tspan>:<tspan class="dir">~</tspan>$ <tspan class="cmd">neofetch</tspan></tspan>
        <tspan x="280" dy="28"><tspan class="key">Role</tspan>       <tspan class="val">~ Developer &amp; Minecraft Architect</tspan></tspan>
        <tspan x="280" dy="24"><tspan class="key">Base</tspan>       <tspan class="val">~ El Ejido, Andalusia</tspan></tspan>
        <tspan x="280" dy="24"><tspan class="key">Stack</tspan>      <tspan class="val">~ HTML, CSS, Python, VS Code</tspan></tspan>
        <tspan x="280" dy="24"><tspan class="key">Gaming</tspan>     <tspan class="val">~ Minecraft 1.20.1 (Forge, Create, CTOV)</tspan></tspan>
        <tspan x="280" dy="24"><tspan class="key">Projects</tspan>   <tspan class="val">~ Web-based Idle Clicker Games</tspan></tspan>
        
        <tspan x="280" dy="35">
            <tspan fill="#ff7b72">███</tspan> <tspan fill="#ffa657">███</tspan> <tspan fill="#3fb950">███</tspan> <tspan fill="#a5d6ff">███</tspan> <tspan fill="#79c0ff">███</tspan> <tspan fill="#d2a8ff">███</tspan>
        </tspan>
    </text>
    </svg>"""
    with open("terminal.svg", "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    create_terminal()
