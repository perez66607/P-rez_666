import json
import os

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

def render_svg():
    if not os.path.exists("data/contributions.json"):
        print("No hay datos.")
        return
        
    with open("data/contributions.json", "r") as f:
        days = json.load(f)
        
    total_contribs = sum(d["count"] for d in days)
    
    svg_width = 860
    svg_height = 145
    
    svg = [
        f'<svg width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">',
        '<style>',
        '  rect { shape-rendering: crispEdges; rx: 3px; ry: 3px; transition: all 0.3s ease; }',
        '  text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 11px; fill: #8b949e; }',
        '</style>',
        '<rect width="100%" height="100%" fill="#0d1117" rx="6"/>'
    ]
    
    cell_size = 11
    cell_gap = 4
    x_offset = 20
    y_offset = 25
    
    for i, day in enumerate(days):
        col = i // 7
        row = i % 7
        
        cx = x_offset + col * (cell_size + cell_gap)
        cy = y_offset + row * (cell_size + cell_gap)
        
        level = day["level"]
        color = PALETTE[level if level < len(PALETTE) else 5]
        date = day["date"]
        count = day["count"]
        
        svg.append(f'  <rect x="{cx}" y="{cy}" width="{cell_size}" height="{cell_size}" fill="{color}">')
        svg.append(f'    <title>{count} contributions on {date}</title>')
        svg.append(f'  </rect>')
        
    svg.append(f'  <text x="{x_offset}" y="130">{total_contribs} contributions in the last year</text>')
    svg.append('</svg>')
    
    with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(svg))

if __name__ == "__main__":
    render_svg()
