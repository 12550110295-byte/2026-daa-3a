from code01_puzzle_slider.models.posisi import Posisi
from code01_puzzle_slider.services.bfs_solver import BFSSolver


def main():
    awal = Posisi((8,4,2,6,5,7,1,3,0))
    akhir = Posisi((1,2,3,4,5,6,7,8,0))
    solver = BFSSolver(awal, akhir)
    solver.solve()
    solver.displaySteps()


if __name__ == "__main__":
    main()