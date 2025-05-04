# gps/parsers/wialon_txt_parser.py
import json

def dmm_to_dd(dmm, direction):
    degrees = int(float(dmm) / 100)
    minutes = float(dmm) - degrees * 100
    dd = degrees + minutes / 60
    return -dd if direction in ['S', 'W'] else dd

def parse_wialon_log_to_geojson(file_path):
    features = []
    with open(file_path, 'r') as f:
        for line in f:
            if not line.startswith('$GPRMC'):
                continue
            parts = line.strip().split(',')
            if len(parts) < 7 or parts[2] != 'A':
                continue
            try:
                lat = dmm_to_dd(parts[3], parts[4])
                lon = dmm_to_dd(parts[5], parts[6])
                time = parts[1]
                date = parts[9]
                iso_datetime = f"20{date[4:6]}-{date[2:4]}-{date[0:2]}T{time[0:2]}:{time[2:4]}:{time[4:6]}"
                features.append({
                    "type": "Feature",
                    "geometry": {"type": "Point", "coordinates": [lon, lat]},
                    "properties": {"time": iso_datetime}
                })
            except:
                continue
    return {
        "type": "FeatureCollection",
        "features": features
    }
