from pathlib import Path
import argparse
import os
import runpy
import sys


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the Kalman object tracking demo without GUI windows."
    )
    parser.add_argument(
        "--output",
        default="plots/headless_run.png",
        help="Path where the final plot image will be saved.",
    )
    parser.add_argument(
        "--video",
        default="ball4.mov",
        help="Input video name or path. Example: ball5 or videos/ball5.mov.",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    video_arg = Path(args.video)
    if not video_arg.suffix:
        video_arg = video_arg.with_suffix(".mov")
    if video_arg.is_absolute():
        video_path = video_arg
    elif video_arg.exists():
        video_path = video_arg.resolve()
    elif (root / "videos" / video_arg).exists():
        video_path = (root / "videos" / video_arg).resolve()
    else:
        video_path = (root / video_arg).resolve()

    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = root / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)

    os.environ.setdefault("MPLCONFIGDIR", "/private/tmp")
    os.environ["KALMAN_VIDEO"] = str(video_path)

    import matplotlib

    matplotlib.use("Agg")

    import cv2
    import matplotlib.pyplot as plt

    cv2.imshow = lambda *args, **kwargs: None
    cv2.waitKey = lambda *args, **kwargs: 1
    cv2.destroyAllWindows = lambda *args, **kwargs: None

    def save_plot(*args, **kwargs):
        plt.tight_layout()
        plt.savefig(output_path, dpi=160)
        print(f"saved {output_path}")

    plt.show = save_plot
    plt.ginput = lambda *args, **kwargs: []

    sys.path.insert(0, str(root / "kalman"))

    old_cwd = Path.cwd()
    try:
        os.chdir(root / "videos")
        runpy.run_path(str(root / "kalman" / "main.py"), run_name="__main__")
    finally:
        os.chdir(old_cwd)


if __name__ == "__main__":
    main()
