import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'FastAPI Predictor',
      theme: ThemeData(
        primarySwatch: Colors.teal,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final TextEditingController hoursStudiedController = TextEditingController();
  final TextEditingController previousScoresController = TextEditingController();
  final TextEditingController sleepHoursController = TextEditingController();
  final TextEditingController samplePapersController = TextEditingController();

  String result = "";

  Future<void> predictPerformance() async {
    final response = await http.post(
      Uri.parse('https://alu-machine-learning-lfkq.onrender.com/predict'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(<String, dynamic>{
        'hours_studied': double.parse(hoursStudiedController.text),
        'previous_scores': double.parse(previousScoresController.text),
        'sleep_hours': double.parse(sleepHoursController.text),
        'sample_question_papers_practiced': int.parse(samplePapersController.text),
      }),
    );

    if (response.statusCode == 200) {
      setState(() {
        result = jsonDecode(response.body)['performance_index'].toString();
      });
    } else {
      throw Exception('Failed to get prediction');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('FastAPI Predictor'),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              'Enter the details below',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 20),
            _buildTextField(
              controller: hoursStudiedController,
              labelText: 'Hours Studied',
              icon: Icons.access_time,
            ),
            SizedBox(height: 20),
            _buildTextField(
              controller: previousScoresController,
              labelText: 'Previous Scores',
              icon: Icons.score,
            ),
            SizedBox(height: 20),
            _buildTextField(
              controller: sleepHoursController,
              labelText: 'Sleep Hours',
              icon: Icons.bedtime,
            ),
            SizedBox(height: 20),
            _buildTextField(
              controller: samplePapersController,
              labelText: 'Sample Question Papers Practiced',
              icon: Icons.book,
            ),
            SizedBox(height: 40),
            ElevatedButton(
              onPressed: predictPerformance,
              child: Padding(
                padding: const EdgeInsets.symmetric(vertical: 12.0, horizontal: 24.0),
                child: Text(
                  'Predict Performance Index',
                  style: TextStyle(fontSize: 18),
                ),
              ),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.teal,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(20),
                ),
              ),
            ),
            SizedBox(height: 20),
            Text(
              result.isEmpty ? 'Enter values to get the prediction' : 'Performance Index: $result',
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.teal),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildTextField({required TextEditingController controller, required String labelText, required IconData icon}) {
    return TextField(
      controller: controller,
      decoration: InputDecoration(
        labelText: labelText,
        prefixIcon: Icon(icon),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
      keyboardType: TextInputType.number,
    );
  }
}
