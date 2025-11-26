!pip install folium

import folium
from IPython.display import IFrame
from google.colab import files

# Your locations: (lat, lng, name)
locations = [
    (23.110658270701773, 79.97737842171905, "akta martket"),
    (23.194915321703323, 79.99488598226195, "vfj mode"),
    (23.223990538285705, 79.96123267250091, "richhai tiraha"),
    (23.20425676489465, 79.88071824233417, "patan bypass"),
    (23.154980728972355, 79.86516053802765, "Andhmook bypass"),
    (23.225380542339273, 79.89477518601089, "katangi baypass"),
    (23.13128328590553, 79.86389318400002, "lamheta bypass"),
]

# Compute map center
center_lat = sum(lat for lat, lng, name in locations) / len(locations)
center_lng = sum(lng for lat, lng, name in locations) / len(locations)

# Create Folium map
m = folium.Map(location=[center_lat, center_lng], zoom_start=12)

# Add markers with tooltip and popup
for lat, lng, name in locations:
    folium.Marker(
        location=[lat, lng],
        tooltip=name,
        popup=name
    ).add_to(m)

# Save map as HTML
html_file = "named_map.html"
m.save(html_file)

# Display map inline in Colab notebook
display(IFrame(html_file, width=700, height=500))

# Provide download link so user can open in browser manually
files.download(html_file)
