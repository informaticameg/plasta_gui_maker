#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from maker import add_maker_simple as maker
import os
import md5

class TestAddMaker(unittest.TestCase):

    def setUp(self):
        self.destinoUI = os.path.expanduser("~") + '/prueba.ui'

    def tearDown(self):
        os.remove( self.destinoUI )

    def testGenerarUISimple(self):
        # codigo md5 del xml resultante del xml generado para este ejemplo
        md5_mxl_ui = '966a9506aa597e137c1f1bdde8d9bec9'
        widgets = {0: {u'nombre': u'QLineEdit'}, 1: {u'apellido': u'QLineEdit'}, 2: {u'direccion': u'QLineEdit'}}
        botones = {'bt_limpiar': False, 'bt_cancelar_aceptar': False, 'bt_salir_guardar': True, 'bt_salir_aceptar': False}
        opciones = {'tipo': 'Dialog', 'generar_plantilla': False}

        self.assertEqual(True, maker.generarUI(self.destinoUI, widgets, botones, opciones) )

        # prueba que el xml md5 sea correcto con una comprobacion md5
        f = open( self.destinoUI, 'r')
        xml = f.read()
        f.close()

        self.assertEqual(md5_mxl_ui, md5.new( xml ).hexdigest())

    def testGenerarUIWidgetsVarios(self):
        # codigo md5 del xml resultante del xml generado para este ejemplo
        md5_mxl_ui = 'd67da331818b28ebf660f733a9eae8e1'
        widgets = {
        0: {u'nombre': u'QLineEdit'},
        1: {u'apellido': u'QSpinBox'},
        2: {u'direccion': u'QCheckBox'},
        3: {u'email': u'QDateEdit'},
        4: {u'sexo': u'QComboBox'},
        5: {u'fecha_cumpleanios': u'QRadioButton'}
        }
        botones = {'bt_limpiar': False, 'bt_cancelar_aceptar': False, 'bt_salir_guardar': True, 'bt_salir_aceptar': False}
        opciones = {'tipo': 'Dialog', 'generar_plantilla': False}

        self.assertEqual(True, maker.generarUI(self.destinoUI, widgets, botones, opciones) )

        # prueba que el xml md5 sea correcto con una comprobacion md5
        f = open( self.destinoUI, 'r')
        xml = f.read()
        f.close()

        self.assertEqual(md5_mxl_ui, md5.new( xml ).hexdigest())

if __name__ == "__main__":
    unittest.main()