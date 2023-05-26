var wms_layers = [];


        var lyr_GoogleSatellite_0 = new ol.layer.Tile({
            'title': 'Google Satellite',
            'type': 'base',
            'opacity': 1.000000,
            
            
            source: new ol.source.XYZ({
    attributions: ' ',
                url: 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}'
            })
        });
var format_EA_Global_ID_v3_1 = new ol.format.GeoJSON();
var features_EA_Global_ID_v3_1 = format_EA_Global_ID_v3_1.readFeatures(json_EA_Global_ID_v3_1, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_EA_Global_ID_v3_1 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_EA_Global_ID_v3_1.addFeatures(features_EA_Global_ID_v3_1);
var lyr_EA_Global_ID_v3_1 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_EA_Global_ID_v3_1, 
                style: style_EA_Global_ID_v3_1,
                interactive: true,
                title: '<img src="styles/legend/EA_Global_ID_v3_1.png" /> EA_Global_ID_v3'
            });
var format_Admin_2_2 = new ol.format.GeoJSON();
var features_Admin_2_2 = format_Admin_2_2.readFeatures(json_Admin_2_2, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_Admin_2_2 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_Admin_2_2.addFeatures(features_Admin_2_2);
var lyr_Admin_2_2 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_Admin_2_2, 
                style: style_Admin_2_2,
                interactive: true,
                title: '<img src="styles/legend/Admin_2_2.png" /> Admin_2'
            });
var format_Admin_1_3 = new ol.format.GeoJSON();
var features_Admin_1_3 = format_Admin_1_3.readFeatures(json_Admin_1_3, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_Admin_1_3 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_Admin_1_3.addFeatures(features_Admin_1_3);
var lyr_Admin_1_3 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_Admin_1_3, 
                style: style_Admin_1_3,
                interactive: true,
                title: '<img src="styles/legend/Admin_1_3.png" /> Admin_1'
            });

lyr_GoogleSatellite_0.setVisible(true);lyr_EA_Global_ID_v3_1.setVisible(true);lyr_Admin_2_2.setVisible(true);lyr_Admin_1_3.setVisible(true);
var layersList = [lyr_GoogleSatellite_0,lyr_EA_Global_ID_v3_1,lyr_Admin_2_2,lyr_Admin_1_3];
lyr_EA_Global_ID_v3_1.set('fieldAliases', {'admin2Name': 'admin2Name', 'admin2Pcod': 'admin2Pcod', 'admin2RefN': 'admin2RefN', 'admin2AltN': 'admin2AltN', 'admin1Name': 'admin1Name', 'admin1Pcod': 'admin1Pcod', 'admin0Name': 'admin0Name', 'admin0Pcod': 'admin0Pcod', 'SUM_1': 'SUM_1', 'Sum_ID': 'Sum_ID', 'SUM_Pop': 'SUM_Pop', 'OBJECTID_J': 'OBJECTID_J', 'Selected': 'Selected', 'admin2Na_1': 'admin2Na_1', 'admin2Pc_1': 'admin2Pc_1', 'admin1Na_1': 'admin1Na_1', 'admin1Pc_1': 'admin1Pc_1', 'admin0Na_1': 'admin0Na_1', 'admin0Pc_1': 'admin0Pc_1', 'IND_POP': 'IND_POP', 'EA_CODE': 'EA_CODE', 'HH_POP': 'HH_POP', 'Random_sor': 'Random_sor', 'Cumulative': 'Cumulative', 'Interval': 'Interval', 'random_sta': 'random_sta', 'Selected_o': 'Selected_o', 'Selected_1': 'Selected_1', 'SUM_Pop_Jo': 'SUM_Pop_Jo', 'GlobalID': 'GlobalID', 'ZONE_CODE': 'ZONE_CODE', 'SUM_12': 'SUM_12', 'SUM_12_13': 'SUM_12_13', });
lyr_Admin_2_2.set('fieldAliases', {'OBJECTID_1': 'OBJECTID_1', 'admin2Name': 'admin2Name', 'admin2Pcod': 'admin2Pcod', 'admin2RefN': 'admin2RefN', 'admin2AltN': 'admin2AltN', 'admin2Al_1': 'admin2Al_1', 'admin1Name': 'admin1Name', 'admin1Pcod': 'admin1Pcod', 'admin0Name': 'admin0Name', 'admin0Pcod': 'admin0Pcod', 'date': 'date', 'validOn': 'validOn', 'ValidTo': 'ValidTo', 'Shape_Leng': 'Shape_Leng', 'Shape_Area': 'Shape_Area', 'district_r': 'district_r', });
lyr_Admin_1_3.set('fieldAliases', {'OBJECTID': 'OBJECTID', 'admin1Name': 'admin1Name', 'admin1Pcod': 'admin1Pcod', 'admin1RefN': 'admin1RefN', 'admin1AltN': 'admin1AltN', 'admin1Al_1': 'admin1Al_1', 'admin0Name': 'admin0Name', 'admin0Pcod': 'admin0Pcod', 'date': 'date', 'validOn': 'validOn', 'validTo': 'validTo', 'Shape_Leng': 'Shape_Leng', 'Shape_Area': 'Shape_Area', });
lyr_EA_Global_ID_v3_1.set('fieldImages', {'admin2Name': 'TextEdit', 'admin2Pcod': 'TextEdit', 'admin2RefN': 'TextEdit', 'admin2AltN': 'TextEdit', 'admin1Name': 'TextEdit', 'admin1Pcod': 'TextEdit', 'admin0Name': 'TextEdit', 'admin0Pcod': 'TextEdit', 'SUM_1': 'TextEdit', 'Sum_ID': 'TextEdit', 'SUM_Pop': 'TextEdit', 'OBJECTID_J': 'TextEdit', 'Selected': 'TextEdit', 'admin2Na_1': 'TextEdit', 'admin2Pc_1': 'TextEdit', 'admin1Na_1': 'TextEdit', 'admin1Pc_1': 'TextEdit', 'admin0Na_1': 'TextEdit', 'admin0Pc_1': 'TextEdit', 'IND_POP': 'TextEdit', 'EA_CODE': 'TextEdit', 'HH_POP': 'TextEdit', 'Random_sor': 'TextEdit', 'Cumulative': 'TextEdit', 'Interval': 'TextEdit', 'random_sta': 'TextEdit', 'Selected_o': 'TextEdit', 'Selected_1': 'TextEdit', 'SUM_Pop_Jo': 'TextEdit', 'GlobalID': 'TextEdit', 'ZONE_CODE': 'TextEdit', 'SUM_12': 'TextEdit', 'SUM_12_13': 'TextEdit', });
lyr_Admin_2_2.set('fieldImages', {'OBJECTID_1': 'Range', 'admin2Name': 'TextEdit', 'admin2Pcod': 'TextEdit', 'admin2RefN': 'TextEdit', 'admin2AltN': 'TextEdit', 'admin2Al_1': 'TextEdit', 'admin1Name': 'TextEdit', 'admin1Pcod': 'TextEdit', 'admin0Name': 'TextEdit', 'admin0Pcod': 'TextEdit', 'date': 'DateTime', 'validOn': 'DateTime', 'ValidTo': 'DateTime', 'Shape_Leng': 'TextEdit', 'Shape_Area': 'TextEdit', 'district_r': 'TextEdit', });
lyr_Admin_1_3.set('fieldImages', {'OBJECTID': 'Range', 'admin1Name': 'TextEdit', 'admin1Pcod': 'TextEdit', 'admin1RefN': 'TextEdit', 'admin1AltN': 'TextEdit', 'admin1Al_1': 'TextEdit', 'admin0Name': 'TextEdit', 'admin0Pcod': 'TextEdit', 'date': 'DateTime', 'validOn': 'DateTime', 'validTo': 'DateTime', 'Shape_Leng': 'TextEdit', 'Shape_Area': 'TextEdit', });
lyr_EA_Global_ID_v3_1.set('fieldLabels', {'admin2Name': 'no label', 'admin2Pcod': 'no label', 'admin2RefN': 'no label', 'admin2AltN': 'no label', 'admin1Name': 'no label', 'admin1Pcod': 'no label', 'admin0Name': 'no label', 'admin0Pcod': 'no label', 'SUM_1': 'no label', 'Sum_ID': 'no label', 'SUM_Pop': 'no label', 'OBJECTID_J': 'no label', 'Selected': 'no label', 'admin2Na_1': 'no label', 'admin2Pc_1': 'no label', 'admin1Na_1': 'no label', 'admin1Pc_1': 'no label', 'admin0Na_1': 'no label', 'admin0Pc_1': 'no label', 'IND_POP': 'no label', 'EA_CODE': 'no label', 'HH_POP': 'no label', 'Random_sor': 'no label', 'Cumulative': 'no label', 'Interval': 'no label', 'random_sta': 'no label', 'Selected_o': 'no label', 'Selected_1': 'no label', 'SUM_Pop_Jo': 'no label', 'GlobalID': 'no label', 'ZONE_CODE': 'no label', 'SUM_12': 'no label', 'SUM_12_13': 'no label', });
lyr_Admin_2_2.set('fieldLabels', {'OBJECTID_1': 'no label', 'admin2Name': 'no label', 'admin2Pcod': 'no label', 'admin2RefN': 'no label', 'admin2AltN': 'no label', 'admin2Al_1': 'no label', 'admin1Name': 'no label', 'admin1Pcod': 'no label', 'admin0Name': 'no label', 'admin0Pcod': 'no label', 'date': 'no label', 'validOn': 'no label', 'ValidTo': 'no label', 'Shape_Leng': 'no label', 'Shape_Area': 'no label', 'district_r': 'no label', });
lyr_Admin_1_3.set('fieldLabels', {'OBJECTID': 'no label', 'admin1Name': 'no label', 'admin1Pcod': 'no label', 'admin1RefN': 'no label', 'admin1AltN': 'no label', 'admin1Al_1': 'no label', 'admin0Name': 'no label', 'admin0Pcod': 'no label', 'date': 'no label', 'validOn': 'no label', 'validTo': 'no label', 'Shape_Leng': 'no label', 'Shape_Area': 'no label', });
lyr_Admin_1_3.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});