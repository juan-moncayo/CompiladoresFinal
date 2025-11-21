# CompiladoresFinal

# Test válido
python main.py tests/test01_basico.txt out1.py
python out1.py

python main.py tests/test02_multiple.txt out2.py
python out2.py

# Test error
python main.py tests/error01_inexistente.txt

python main.py tests/error02_duplicada.txt

# Test Automaticos
python run_tests.py

