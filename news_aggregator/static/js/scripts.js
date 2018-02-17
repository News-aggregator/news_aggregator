function initMap() {
            var map = new google.maps.Map(document.getElementById('map'), {
                center: {lat: 39.8333333, lng: -98.585522},
                zoom: 4,
                styles: [
                    {elementType: 'water', stylers: [{color: "#444444"}]},
                    {elementType: 'labels', stylers: [{ visibility: "off"}]},
                    {
                        featureType: "poi",
                        elementType: "all",
                        stylers: [{visibility: "off"}]
                    },
                    {
                        featureType: "road",
                        elementType: "all",
                        stylers: [{visibility: "off"}]
                    },
                    {
                        featureType: "Transit",
                        elementType: "all",
                        stylers: [{visbility: "off"}]
                    },

                    {
                        featureType: 'administrative',
                        elementType: 'labels',
                        stylers: [{visibility: "off"}]
                    },
                    {
                        featureType: 'administrative',
                        elementType: 'geometry.stroke',
                        stylers: [{color: "#FFFFFF"}]
                    },
                    {
                        featureType: 'landscape',
                        elementType: 'all',
                        stylers: [{color: "#555555"}]
                    }
                ]
            });
        }