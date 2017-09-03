
"""------------------- Direct to change to Game START -----------------------"""
      # Set up test replay on Simple64 as RandomAgent/test.SC2Replay
      map_inst = maps.get("Simple64")
      if map_inst.game_steps_per_episode:
        max_episode_steps = map_inst.game_steps_per_episode

      create = sc_pb.RequestCreateGame(
            realtime=FLAGS.realtime,
            disable_fog=FLAGS.disable_fog,
            local_map=sc_pb.LocalMap(map_path=map_inst.path,
                                     map_data=map_inst.data(run_config)))
      create.player_setup.add(type=sc_pb.Participant)
      create.player_setup.add(type=sc_pb.Computer,
                            race=sc2_env.races[FLAGS.bot_race],
                            difficulty=sc2_env.difficulties[FLAGS.difficulty])

      join = sc_pb.RequestJoinGame(race=sc2_env.races[FLAGS.user_race],
                                 options=interface)
      controller.create_game(create)
      controller.join_game(join)

      # Extra to render doesn't work 
      renderer = renderer_human.RendererHuman(
          fps=FLAGS.fps, step_mul=FLAGS.step_mul,
          render_sync=FLAGS.render_sync)
      renderer.run(
          run_config, controller, max_game_steps=FLAGS.max_game_steps,
          game_steps_per_episode=max_episode_steps,
          save_replay=FLAGS.save_replay)
"""------------------- Direct to change to Game END -------------------------"""
