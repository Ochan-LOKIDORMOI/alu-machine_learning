#!/usr/bin/env python3
"""Put it all together and what do you get"""

import tensorflow as tf
import numpy as np

def model(Data_train, Data_valid, layers,
          activations, alpha=0.001, beta1=0.9,
          beta2=0.999, epsilon=1e-8,
          decay_rate=1, batch_size=32, epochs=5,
          save_path='/tmp/model.ckpt'):
    # Unpacking the training and validation data
    X_train, Y_train = Data_train
    X_valid, Y_valid = Data_valid
    
    # Get input shape from X_train
    input_shape = X_train.shape[1:]
    
    # Build the model
    model = tf.keras.Sequential()
    
    # Add input layer
    model.add(tf.keras.layers.InputLayer(input_shape=input_shape))
    
    # Adding the hidden layers with activation functions and batch normalization
    for i, (layer_size, activation) in enumerate(zip(layers, activations)):
        model.add(tf.keras.layers.Dense(units=layer_size, activation=None,
                                        kernel_initializer='he_normal'))
        model.add(tf.keras.layers.BatchNormalization())
        model.add(tf.keras.layers.Activation(activation))
    
    # Output layer (assuming a softmax output for classification)
    model.add(tf.keras.layers.Dense(units=Y_train.shape[1], activation='softmax'))
    
    # Adam Optimizer with learning rate schedule (decay)
    global_step = tf.Variable(0, trainable=False)
    lr_schedule = tf.keras.optimizers.schedules.InverseTimeDecay(
        alpha,
        decay_steps=1,
        decay_rate=decay_rate,
        staircase=True
    )
    optimizer = tf.keras.optimizers.Adam(learning_rate=lr_schedule,
                                         beta_1=beta1, beta_2=beta2,
                                         epsilon=epsilon)
    
    # Compile the model with loss, optimizer, and metrics
    model.compile(optimizer=optimizer,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
    # Training loop with shuffling and mini-batch gradient descent
    m = X_train.shape[0]
    steps_per_epoch = int(np.ceil(m / batch_size))
    
    # Define a callback to save the model
    checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(filepath=save_path,
                                                             save_best_only=True)

    # Loop over the epochs
    for epoch in range(epochs):
        print(f"After {epoch} epochs:")
        
        # Shuffle the data before each epoch
        indices = np.random.permutation(m)
        X_train_shuffled = X_train[indices]
        Y_train_shuffled = Y_train[indices]
        
        # Mini-batch gradient descent
        for step in range(steps_per_epoch):
            start = step * batch_size
            end = min(start + batch_size, m)
            X_batch = X_train_shuffled[start:end]
            Y_batch = Y_train_shuffled[start:end]
            
            # Train on batch
            history = model.train_on_batch(X_batch, Y_batch)
            
            if step % 100 == 0:
                step_cost, step_accuracy = history
                print(f"\tStep {step}:")
                print(f"\t\tCost: {step_cost}")
                print(f"\t\tAccuracy: {step_accuracy}")
        
        # Evaluate on full training and validation data after each epoch
        train_cost, train_accuracy = model.evaluate(X_train, Y_train, verbose=0)
        valid_cost, valid_accuracy = model.evaluate(X_valid, Y_valid, verbose=0)
        
        print(f"\tTraining Cost: {train_cost}")
        print(f"\tTraining Accuracy: {train_accuracy}")
        print(f"\tValidation Cost: {valid_cost}")
        print(f"\tValidation Accuracy: {valid_accuracy}")
    
    # Save the model at the end of training
    model.save(save_path)
    
    return save_path
