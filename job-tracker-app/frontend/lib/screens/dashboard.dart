import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/job_provider.dart';

class DashboardScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final provider = Provider.of<JobProvider>(context);

    return Scaffold(
      appBar: AppBar(title: Text("Job Tracker")),

      body: provider.loading
          ? Center(child: CircularProgressIndicator())
          : ListView.builder(
              itemCount: provider.jobs.length,
              itemBuilder: (context, index) {
                final job = provider.jobs[index];

                return ListTile(
                  title: Text(job.title),
                  subtitle: Text(job.company),
                  trailing: Text(job.status),
                );
              },
            ),

      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.pushNamed(context, "/add");
        },
        child: Icon(Icons.add),
      ),
    );
  }
}
