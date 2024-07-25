import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Students Performance App Predictor',
      theme: ThemeData(
        primarySwatch: Colors.teal,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

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
      Uri.parse('https://alu-machine-learning-1-hw3s.onrender.com/predict'),
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
        title: const Text('Students Performance App Predictor'),
        backgroundColor: const Color.fromARGB(255, 64, 169, 245),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'Enter the details below',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 25),
            _buildTextField(
              controller: hoursStudiedController,
              labelText: 'Hours Studied',
              icon: Icons.access_time,
            ),
            const SizedBox(height: 25),
            _buildTextField(
              controller: previousScoresController,
              labelText: 'Previous Scores',
              icon: Icons.score,
            ),
            const SizedBox(height: 25),
            _buildTextField(
              controller: sleepHoursController,
              labelText: 'Sleep Hours',
              icon: Icons.bedtime,
            ),
            const SizedBox(height: 25),
            _buildTextField(
              controller: samplePapersController,
              labelText: 'Sample Question Papers Practiced',
              icon: Icons.book,
            ),
            const SizedBox(height: 40),
            ElevatedButton(
              onPressed: predictPerformance,
              style: ElevatedButton.styleFrom(
                backgroundColor: const Color.fromARGB(255, 64, 169, 245),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(20),
                ),
              ),
              child: const Padding(
                padding: EdgeInsets.symmetric(vertical: 12.0, horizontal: 24.0),
                child: Text(
                  'Predict',
                  style: TextStyle(fontSize: 20),
                ),
              ),
            ),
            const SizedBox(height: 20),
            Text(
              result.isEmpty ? 'Enter values to get the prediction' : 'Performance Index: $result',
              style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.teal),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildTextField({required TextEditingController controller, required String labelText, required IconData icon}) {
    return TextField(
      controller: controller,
      style: const TextStyle(fontSize: 18), 
      decoration: InputDecoration(
        labelText: labelText,
        labelStyle: const TextStyle(fontSize: 18),
        prefixIcon: Icon(icon),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
      keyboardType: TextInputType.number,
    );
  }
}
